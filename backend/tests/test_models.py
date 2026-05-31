import pytest
from pydantic import ValidationError

from backend.core.models import Coordinates, OmegaSequence, PaletteItem, PhaseMatch


def make_palette_item(index: int) -> PaletteItem:
    return PaletteItem(
        operator_id=f"operator_{index}",
        symbol=f"S{index}",
        value=f"value_{index}",
        coordinates=Coordinates(A=0.5, S=0.5, T=0.5, E=0.5),
        confidence=0.5,
        synthetic=False,
    )


def make_phase_match(index: int) -> PhaseMatch:
    return PhaseMatch(
        operator_id=f"operator_{index}",
        display_symbol=f"S{index}",
        source_text=f"segment_{index}",
        start_offset=index,
        end_offset=index + 1,
        confidence=0.5,
        synthetic=False,
        markers=[],
    )


def test_coordinates_validate_range() -> None:
    with pytest.raises(ValidationError):
        Coordinates(A=1.2, S=0.5, T=0.5, E=0.5)


def test_omega_sequence_requires_exactly_seven_items() -> None:
    with pytest.raises(ValidationError):
        OmegaSequence(
            palette=[make_palette_item(i) for i in range(6)],
            phase_matches=[make_phase_match(i) for i in range(7)],
        )
