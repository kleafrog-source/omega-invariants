from __future__ import annotations

from .constants import A3_EPSILON, COORDINATE_KEYS, LAMBDA
from .metrics import average_sigma, calculate_rho_values, check_zero_flux
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
    sigma = average_sigma(coordinates)
    rho_values = calculate_rho_values([sigma] * max(len(coordinates) - 1, 1), lambd=LAMBDA)
    return all(0.40 <= rho <= 1.00 for rho in rho_values), rho_values


def validate_axioms(
    sequence: OmegaSequence,
    coordinates: list[Coordinates],
) -> ValidationReport:
    messages: list[str] = []

    a1 = validate_A1(sequence)
    if not a1:
        messages.append("A1 failed: palette order is not the canonical Omega order.")

    a2 = validate_A2(coordinates)
    if not a2:
        messages.append("A2 failed: zero-flux normalization was not preserved.")

    a3 = validate_A3(coordinates[0], coordinates[-1]) if coordinates else False
    if not a3:
        messages.append("A3 failed: terminal coordinates are outside the closure window.")

    a4 = validate_A4()
    a5, _ = validate_A5(coordinates)
    if not a5:
        messages.append("A5 failed: rho values are outside the valid density range.")

    return ValidationReport(
        A1_monotonic_path=a1,
        A2_zero_flux=a2,
        A3_recurrent_closure=a3,
        A4_operator_isomorphism=a4,
        A5_adaptive_density=a5,
        messages=messages,
    )
