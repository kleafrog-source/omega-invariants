from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from .constants import COORDINATE_KEYS


class Coordinates(BaseModel):
    model_config = ConfigDict(extra="forbid")

    A: float = Field(ge=0.0, le=1.0)
    S: float = Field(ge=0.0, le=1.0)
    T: float = Field(ge=0.0, le=1.0)
    E: float = Field(ge=0.0, le=1.0)

    def as_dict(self) -> dict[str, float]:
        return {key: getattr(self, key) for key in COORDINATE_KEYS}


class OperatorDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    internal_id: str
    ascii_key: str
    display_symbol: str
    label: str
    color: str
    phase_index: int = Field(ge=0, le=6)


class PhaseMatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    operator_id: str
    display_symbol: str
    source_text: str
    start_offset: int | None = Field(default=None, ge=0)
    end_offset: int | None = Field(default=None, ge=0)
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    synthetic: bool = False
    markers: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_offsets(self) -> "PhaseMatch":
        if (
            self.start_offset is not None
            and self.end_offset is not None
            and self.end_offset < self.start_offset
        ):
            raise ValueError("end_offset must be greater than or equal to start_offset")
        return self


class PaletteItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    operator_id: str
    symbol: str
    value: str
    coordinates: Coordinates
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    synthetic: bool = False


class OmegaSequence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    palette: list[PaletteItem]
    phase_matches: list[PhaseMatch]
    recursion_depth: int = Field(default=0, ge=0)
    domain: str = "generic"

    @field_validator("palette")
    @classmethod
    def validate_palette_length(cls, palette: list[PaletteItem]) -> list[PaletteItem]:
        if len(palette) != 7:
            raise ValueError("palette must contain exactly 7 items")
        return palette

    @field_validator("phase_matches")
    @classmethod
    def validate_phase_match_length(
        cls, phase_matches: list[PhaseMatch]
    ) -> list[PhaseMatch]:
        if len(phase_matches) != 7:
            raise ValueError("phase_matches must contain exactly 7 items")
        return phase_matches


class ValidationReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    A1_monotonic_path: bool
    A2_zero_flux: bool
    A3_recurrent_closure: bool
    A4_operator_isomorphism: bool
    A5_adaptive_density: bool
    messages: list[str] = Field(default_factory=list)


class OmegaResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sequence: list[str]
    palette: list[PaletteItem]
    phase_matches: list[PhaseMatch]
    coordinates: list[Coordinates]
    D_metric: float = Field(ge=0.0)
    rho_values: list[float]
    sigma_values: list[float]
    stability_flag: bool
    corrections_applied: list[str] = Field(default_factory=list)
    validation: ValidationReport
