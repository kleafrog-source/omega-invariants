from __future__ import annotations

from typing import Final

from .models import OperatorDefinition


OPERATORS: Final[list[OperatorDefinition]] = [
    OperatorDefinition(
        internal_id="init",
        ascii_key="INIT",
        display_symbol="∂₀",
        label="Initiation",
        color="#ff4d4d",
        phase_index=0,
    ),
    OperatorDefinition(
        internal_id="stabilize",
        ascii_key="STAB",
        display_symbol="≈",
        label="Stabilization",
        color="#8b92a5",
        phase_index=1,
    ),
    OperatorDefinition(
        internal_id="vectorize",
        ascii_key="VECT",
        display_symbol="↑⃗",
        label="Vectorization",
        color="#f2c94c",
        phase_index=2,
    ),
    OperatorDefinition(
        internal_id="commute",
        ascii_key="COMM",
        display_symbol="⇄",
        label="Commutation",
        color="#f2994a",
        phase_index=3,
    ),
    OperatorDefinition(
        internal_id="convolve",
        ascii_key="CONV",
        display_symbol="⊗",
        label="Convolution",
        color="#9b51e0",
        phase_index=4,
    ),
    OperatorDefinition(
        internal_id="relax",
        ascii_key="RLAX",
        display_symbol="↓",
        label="Relaxation",
        color="#27ae60",
        phase_index=5,
    ),
    OperatorDefinition(
        internal_id="focus",
        ascii_key="FOCS",
        display_symbol="∞",
        label="Focusing",
        color="#2d9cdb",
        phase_index=6,
    ),
]

OPERATORS_BY_ID: Final[dict[str, OperatorDefinition]] = {
    operator.internal_id: operator for operator in OPERATORS
}

OPERATORS_BY_ASCII: Final[dict[str, OperatorDefinition]] = {
    operator.ascii_key: operator for operator in OPERATORS
}
