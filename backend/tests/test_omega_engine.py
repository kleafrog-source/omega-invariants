from backend.core.models import Coordinates, OmegaSequence, PaletteItem, PhaseMatch
from backend.core.omega_engine import OmegaEngine
from backend.core.operators import OPERATORS


def make_sequence() -> OmegaSequence:
    palette: list[PaletteItem] = []
    phase_matches: list[PhaseMatch] = []

    stable_coordinate = Coordinates(A=0.5, S=0.5, T=0.5, E=0.5)
    for operator in OPERATORS:
        palette.append(
            PaletteItem(
                operator_id=operator.internal_id,
                symbol=operator.display_symbol,
                value=f"{operator.internal_id}_value",
                coordinates=stable_coordinate,
                confidence=0.8,
                synthetic=False,
            )
        )
        phase_matches.append(
            PhaseMatch(
                operator_id=operator.internal_id,
                display_symbol=operator.display_symbol,
                source_text=f"{operator.label} segment",
                start_offset=operator.phase_index,
                end_offset=operator.phase_index + 1,
                confidence=0.8,
                synthetic=False,
                markers=[],
            )
        )

    return OmegaSequence(palette=palette, phase_matches=phase_matches, recursion_depth=0, domain="generic")


def test_validate_palette_accepts_canonical_sequence() -> None:
    engine = OmegaEngine()
    sequence = make_sequence()
    assert engine.validate_palette(sequence) is True


def test_run_returns_stable_result_for_flat_coordinates() -> None:
    engine = OmegaEngine()
    sequence = make_sequence()
    result = engine.run(sequence)

    assert result.stability_flag is True
    assert result.D_metric == 0.0
    assert result.validation.A1_monotonic_path is True
    assert result.validation.A2_zero_flux is True
    assert result.validation.A3_recurrent_closure is True
    assert result.validation.A5_adaptive_density is True


def test_zero_flux_normalization_closes_terminal_drift() -> None:
    engine = OmegaEngine()
    sequence = make_sequence()
    sequence.palette[-1] = sequence.palette[-1].model_copy(
        update={"coordinates": Coordinates(A=0.7, S=0.4, T=0.6, E=0.2)},
        deep=True,
    )

    result = engine.run(sequence)

    assert result.coordinates[0].A == result.coordinates[-1].A
    assert result.coordinates[0].S == result.coordinates[-1].S
    assert result.coordinates[0].T == result.coordinates[-1].T
    assert result.coordinates[0].E == result.coordinates[-1].E
    assert result.validation.A2_zero_flux is True
    assert result.validation.A3_recurrent_closure is True
