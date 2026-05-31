from __future__ import annotations

import math
from typing import Iterable

from .constants import COORDINATE_KEYS, KAPPA, RHO_MAX, RHO_MIN, WEIGHTS, ZERO_FLUX_TOLERANCE
from .models import Coordinates


def clip(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def density_compensation(sigma: float, lambd: float) -> float:
    return clip(math.exp(-lambd * (sigma**2)), RHO_MIN, RHO_MAX)


def calculate_rho_values(sigmas: Iterable[float], lambd: float) -> list[float]:
    return [density_compensation(sigma=sigma, lambd=lambd) for sigma in sigmas]


def calculate_D(
    coordinates: list[Coordinates],
    sigma_avg: float,
) -> float:
    if len(coordinates) < 2:
        return 0.0

    weighted_delta_sum = 0.0
    for previous, current in zip(coordinates, coordinates[1:]):
        prev_dict = previous.as_dict()
        curr_dict = current.as_dict()
        for key in COORDINATE_KEYS:
            weighted_delta_sum += WEIGHTS[key] * ((curr_dict[key] - prev_dict[key]) ** 2)

    rho_floor = min(calculate_rho_values([sigma_avg], lambd=0.85))
    return math.sqrt(weighted_delta_sum + (KAPPA * (sigma_avg**2))) * (1 - rho_floor)


def check_zero_flux(
    coordinates: list[Coordinates],
    tolerance: float = ZERO_FLUX_TOLERANCE,
) -> bool:
    if len(coordinates) < 2:
        return True

    for key in COORDINATE_KEYS:
        total_delta = 0.0
        for previous, current in zip(coordinates, coordinates[1:]):
            total_delta += getattr(current, key) - getattr(previous, key)
        if abs(total_delta) > tolerance:
            return False
    return True


def normalize_zero_flux(coordinates: list[Coordinates]) -> list[Coordinates]:
    if len(coordinates) < 2:
        return coordinates[:]

    normalized = [coordinate.model_copy(deep=True) for coordinate in coordinates]
    phase_count = len(normalized) - 1

    for key in COORDINATE_KEYS:
        residual = getattr(normalized[-1], key) - getattr(normalized[0], key)
        if abs(residual) <= ZERO_FLUX_TOLERANCE:
            continue

        for index in range(1, len(normalized)):
            correction = residual * (index / phase_count)
            current_value = getattr(normalized[index], key) - correction
            setattr(normalized[index], key, clip(current_value, 0.0, 1.0))

    return normalized


def smooth_coordinates(coordinates: list[Coordinates], rho_values: list[float]) -> list[Coordinates]:
    if len(coordinates) < 3:
        return coordinates[:]

    smoothed = [coordinates[0].model_copy(deep=True)]
    for index in range(1, len(coordinates) - 1):
        previous = coordinates[index - 1]
        current = coordinates[index]
        following = coordinates[index + 1]
        rho = rho_values[min(index - 1, len(rho_values) - 1)]
        smoothing_strength = 1.0 - rho

        values: dict[str, float] = {}
        for key in COORDINATE_KEYS:
            neighbor_mean = (getattr(previous, key) + getattr(following, key)) / 2
            blended = getattr(current, key) * rho + neighbor_mean * smoothing_strength
            values[key] = round(clip(blended, 0.0, 1.0), 6)
        smoothed.append(Coordinates(**values))

    smoothed.append(coordinates[-1].model_copy(deep=True))
    return smoothed


def average_sigma(coordinates: list[Coordinates]) -> float:
    if not coordinates:
        return 0.0

    means = {
        key: sum(getattr(coord, key) for coord in coordinates) / len(coordinates)
        for key in COORDINATE_KEYS
    }

    variance_sum = 0.0
    for key in COORDINATE_KEYS:
        variance_sum += (
            sum((getattr(coord, key) - means[key]) ** 2 for coord in coordinates)
            / len(coordinates)
        )
    return math.sqrt(variance_sum / len(COORDINATE_KEYS))
