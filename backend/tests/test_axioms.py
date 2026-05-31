from core.models import Coordinates, OmegaSequence, PaletteItem, PhaseMatch
from core.axioms import (
    validate_A1_detailed,
    validate_A2_detailed,
    validate_A3_detailed,
    validate_A5_detailed,
)
from core.operators import OPERATORS


def make_sequence() -> OmegaSequence:
    palette = []
    phase_matches = []
    for operator in OPERATORS:
        coords = Coordinates(A=0.5, S=0.5, T=0.5, E=0.5)
        palette.append(
            PaletteItem(
                operator_id=operator.internal_id,
                symbol=operator.display_symbol,
                value=operator.label,
                coordinates=coords,
                confidence=0.8,
                synthetic=False,
            )
        )
        phase_matches.append(
            PhaseMatch(
                operator_id=operator.internal_id,
                display_symbol=operator.display_symbol,
                source_text=operator.label,
                start_offset=operator.phase_index,
                end_offset=operator.phase_index + 1,
                confidence=0.8,
                synthetic=False,
                markers=[],
            )
        )
    return OmegaSequence(palette=palette, phase_matches=phase_matches)


def test_validate_A1_detailed_returns_pass_message() -> None:
    passed, message = validate_A1_detailed(make_sequence())
    assert passed is True
    assert "strict sequential order" in message


def test_validate_A2_detailed_returns_pass_message() -> None:
    coords = [Coordinates(A=0.5, S=0.5, T=0.5, E=0.5) for _ in range(3)]
    passed, message = validate_A2_detailed(coords)
    assert passed is True
    assert "Zero flux verified" in message


def test_validate_A3_detailed_returns_pass_message() -> None:
    passed, message = validate_A3_detailed(
        Coordinates(A=0.5, S=0.5, T=0.5, E=0.5),
        Coordinates(A=0.56, S=0.47, T=0.53, E=0.58),
    )
    assert passed is True
    assert "Terminal within" in message


def test_validate_A5_detailed_reports_variation() -> None:
    coords = [
        Coordinates(A=0.68, S=0.38, T=0.62, E=0.54),
        Coordinates(A=0.46, S=0.58, T=0.44, E=0.42),
        Coordinates(A=0.64, S=0.52, T=0.72, E=0.50),
        Coordinates(A=0.52, S=0.56, T=0.60, E=0.48),
        Coordinates(A=0.58, S=0.74, T=0.57, E=0.58),
        Coordinates(A=0.34, S=0.50, T=0.36, E=0.32),
        Coordinates(A=0.666, S=0.42, T=0.585, E=0.592),
    ]
    passed, message = validate_A5_detailed(coords)
    assert passed is True
    assert "Adaptive density" in message
