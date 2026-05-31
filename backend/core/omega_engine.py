from __future__ import annotations

from .axioms import validate_A5, validate_axioms
from .constants import D_MAX_ACCEPTABLE, MAX_CORRECTION_ITERATIONS
from .metrics import average_sigma, calculate_D, normalize_zero_flux, smooth_coordinates
from .models import Coordinates, OmegaResult, OmegaSequence, PaletteItem


class OmegaEngine:
    def validate_palette(self, sequence: OmegaSequence) -> bool:
        return len(sequence.palette) == 7 and len(sequence.phase_matches) == 7

    def apply_template(self, sequence: OmegaSequence) -> list[str]:
        return [item.symbol for item in sequence.palette]

    def extract_coordinates(self, sequence: OmegaSequence) -> list[Coordinates]:
        return [item.coordinates for item in sequence.palette]

    def calculate_metrics(self, coordinates: list[Coordinates]) -> tuple[float, list[float]]:
        sigma_avg = average_sigma(coordinates)
        d_metric = calculate_D(coordinates=coordinates, sigma_avg=sigma_avg)
        _, rho_values = validate_A5(coordinates)
        return d_metric, rho_values

    def apply_zero_flux_normalization(self, coordinates: list[Coordinates]) -> list[Coordinates]:
        return normalize_zero_flux(coordinates)

    def apply_self_correction(
        self,
        coordinates: list[Coordinates],
        rho_values: list[float],
    ) -> list[Coordinates]:
        corrected = smooth_coordinates(coordinates=coordinates, rho_values=rho_values)
        return normalize_zero_flux(corrected)

    def rebuild_palette(
        self,
        sequence: OmegaSequence,
        coordinates: list[Coordinates],
    ) -> list[PaletteItem]:
        rebuilt: list[PaletteItem] = []
        for item, coordinate in zip(sequence.palette, coordinates):
            rebuilt.append(item.model_copy(update={"coordinates": coordinate}, deep=True))
        return rebuilt

    def run(self, sequence: OmegaSequence) -> OmegaResult:
        if not self.validate_palette(sequence):
            raise ValueError("OmegaSequence must contain exactly 7 palette items and 7 phase matches")

        corrections_applied: list[str] = []
        coordinates = self.apply_zero_flux_normalization(self.extract_coordinates(sequence))
        d_metric, rho_values = self.calculate_metrics(coordinates)

        iteration = 0
        while d_metric > D_MAX_ACCEPTABLE and iteration < MAX_CORRECTION_ITERATIONS:
            coordinates = self.apply_self_correction(coordinates=coordinates, rho_values=rho_values)
            corrections_applied.append(
                f"self_correction_iteration_{iteration + 1}: redistributed local drift and smoothed transitions"
            )
            iteration += 1
            d_metric, rho_values = self.calculate_metrics(coordinates)

        validation = validate_axioms(sequence=sequence, coordinates=coordinates)
        stability_flag = d_metric <= D_MAX_ACCEPTABLE and not validation.messages

        return OmegaResult(
            sequence=self.apply_template(sequence),
            palette=self.rebuild_palette(sequence=sequence, coordinates=coordinates),
            phase_matches=sequence.phase_matches,
            coordinates=coordinates,
            D_metric=d_metric,
            rho_values=rho_values,
            stability_flag=stability_flag,
            corrections_applied=corrections_applied,
            validation=validation,
        )
