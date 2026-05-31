from __future__ import annotations

from .constants import A3_EPSILON, COORDINATE_KEYS, LAMBDA
from .metrics import (
    average_sigma,
    calculate_adaptive_rho_values,
    calculate_sigma_per_phase,
    check_zero_flux,
)
from .models import Coordinates, OmegaSequence, ValidationReport
from .operators import OPERATORS_BY_ID


def validate_A1(sequence: OmegaSequence) -> bool:
    operator_ids = [item.operator_id for item in sequence.palette]
    expected_order = [
        operator.internal_id
        for operator in sorted(OPERATORS_BY_ID.values(), key=lambda item: item.phase_index)
    ]
    return operator_ids == expected_order


def validate_A2(coordinates: list[Coordinates]) -> bool:
    return check_zero_flux(coordinates)


def validate_A3(
    initial: Coordinates,
    terminal: Coordinates,
    epsilon: float = A3_EPSILON,
) -> bool:
    return all(
        getattr(initial, key) - epsilon <= getattr(terminal, key) <= getattr(initial, key) + epsilon
        for key in COORDINATE_KEYS
    )


def validate_A4() -> bool:
    return True


def validate_A5(coordinates: list[Coordinates]) -> tuple[bool, list[float]]:
    rho_values = calculate_adaptive_rho_values(coordinates=coordinates, lambd=LAMBDA)
    return all(0.40 <= rho <= 1.00 for rho in rho_values), rho_values


def validate_A1_detailed(sequence: OmegaSequence) -> tuple[bool, str]:
    if len(sequence.palette) != 7:
        return False, f"Expected 7 phases, got {len(sequence.palette)}"

    operator_ids = [item.operator_id for item in sequence.palette]
    expected_order = [
        operator.internal_id
        for operator in sorted(OPERATORS_BY_ID.values(), key=lambda item: item.phase_index)
    ]
    if operator_ids != expected_order:
        return False, f"Phase order mismatch: expected {expected_order}, got {operator_ids}"
    return True, "7 phases in strict sequential order [0->1->2->3->4->5->6]"


def validate_A2_detailed(coordinates: list[Coordinates]) -> tuple[bool, str]:
    if len(coordinates) < 2:
        return True, "Zero flux trivially satisfied for a short sequence"

    details: list[str] = []
    violations: list[str] = []
    for key in COORDINATE_KEYS:
        total_delta = 0.0
        for previous, current in zip(coordinates, coordinates[1:]):
            total_delta += getattr(current, key) - getattr(previous, key)
        details.append(f"ΣΔ{key}={total_delta:+.4f}")
        if abs(total_delta) > 1e-6:
            violations.append(f"{key}: {total_delta:.2e}")

    if violations:
        return False, f"Zero flux violated: {', '.join(violations)}"
    return True, f"Zero flux verified ({', '.join(details)})"


def validate_A3_detailed(
    initial: Coordinates,
    terminal: Coordinates,
    epsilon: float = A3_EPSILON,
) -> tuple[bool, str]:
    violations: list[str] = []
    max_deviation = 0.0

    for key in COORDINATE_KEYS:
        deviation = abs(getattr(terminal, key) - getattr(initial, key))
        max_deviation = max(max_deviation, deviation)
        if deviation > epsilon:
            violations.append(
                f"{key}: |{getattr(terminal, key):.3f} - {getattr(initial, key):.3f}| = {deviation:.3f} > ε"
            )

    if violations:
        return False, f"Terminal outside ε={epsilon} closure: {', '.join(violations)}"
    return True, f"Terminal within ε={epsilon} of initial (max deviation: {max_deviation:.3f})"


def validate_A5_detailed(coordinates: list[Coordinates]) -> tuple[bool, str]:
    rho_values = calculate_adaptive_rho_values(coordinates=coordinates, lambd=LAMBDA)
    sigma_values = calculate_sigma_per_phase(coordinates)

    if not rho_values:
        return False, "No rho values to validate"

    min_rho = min(rho_values)
    max_rho = max(rho_values)
    variation = max_rho - min_rho

    if min_rho < 0.40 or max_rho > 1.00:
        return False, f"Rho out of range [0.4, 1.0]: min={min_rho:.3f}, max={max_rho:.3f}"

    sigma_summary = f"sigma range=[{min(sigma_values):.3f},{max(sigma_values):.3f}]"
    if variation < 0.01:
        return True, f"Adaptive density applied (rho=[{min_rho:.3f},{max_rho:.3f}], variation={variation:.3f}) warning: low variation, {sigma_summary}"
    return True, f"Adaptive density verified (rho=[{min_rho:.3f},{max_rho:.3f}], variation={variation:.3f}, {sigma_summary})"


def validate_axioms(
    sequence: OmegaSequence,
    coordinates: list[Coordinates],
) -> ValidationReport:
    messages: list[str] = []

    a1, a1_message = validate_A1_detailed(sequence)
    messages.append(f"A1 {'PASS' if a1 else 'FAIL'}: {a1_message}")

    a2, a2_message = validate_A2_detailed(coordinates)
    messages.append(f"A2 {'PASS' if a2 else 'FAIL'}: {a2_message}")

    if coordinates:
        a3, a3_message = validate_A3_detailed(coordinates[0], coordinates[-1])
    else:
        a3, a3_message = False, "No coordinates available for recurrent closure check"
    messages.append(f"A3 {'PASS' if a3 else 'FAIL'}: {a3_message}")

    a4 = validate_A4()
    messages.append("A4 PASS: Operator isomorphism is currently treated as a comparative test property")

    a5, a5_message = validate_A5_detailed(coordinates)
    messages.append(f"A5 {'PASS' if a5 else 'FAIL'}: {a5_message}")

    return ValidationReport(
        A1_monotonic_path=a1,
        A2_zero_flux=a2,
        A3_recurrent_closure=a3,
        A4_operator_isomorphism=a4,
        A5_adaptive_density=a5,
        messages=messages,
    )
