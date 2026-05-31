from core.models import Coordinates
from core.metrics import calculate_adaptive_rho_values, calculate_sigma_per_phase


def test_calculate_sigma_per_phase_returns_values_for_each_phase() -> None:
    coordinates = [
        Coordinates(A=0.65, S=0.40, T=0.60, E=0.52),
        Coordinates(A=0.48, S=0.57, T=0.46, E=0.44),
        Coordinates(A=0.62, S=0.53, T=0.71, E=0.50),
        Coordinates(A=0.51, S=0.56, T=0.61, E=0.49),
    ]

    sigma_values = calculate_sigma_per_phase(coordinates)
    assert len(sigma_values) == len(coordinates)
    assert all(sigma >= 0.0 for sigma in sigma_values)


def test_calculate_adaptive_rho_values_varies_across_transitions() -> None:
    coordinates = [
        Coordinates(A=0.68, S=0.38, T=0.62, E=0.54),
        Coordinates(A=0.46, S=0.58, T=0.44, E=0.42),
        Coordinates(A=0.64, S=0.52, T=0.72, E=0.50),
        Coordinates(A=0.52, S=0.56, T=0.60, E=0.48),
        Coordinates(A=0.58, S=0.74, T=0.57, E=0.58),
        Coordinates(A=0.34, S=0.50, T=0.36, E=0.32),
        Coordinates(A=0.666, S=0.42, T=0.585, E=0.592),
    ]

    rho_values = calculate_adaptive_rho_values(coordinates)
    assert len(rho_values) == len(coordinates) - 1
    assert min(rho_values) >= 0.4
    assert max(rho_values) <= 1.0
    assert max(rho_values) - min(rho_values) >= 0.008
