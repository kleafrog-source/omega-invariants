from __future__ import annotations

import re
from dataclasses import dataclass

from core.constants import MIN_CONFIDENCE_SYNTHETIC
from core.models import Coordinates, OmegaSequence, PaletteItem, PhaseMatch
from core.operators import OPERATORS

from .base_agent import BaseAgent


@dataclass(frozen=True)
class PhasePattern:
    operator_id: str
    keywords: tuple[str, ...]
    markers: tuple[str, ...]


class OfflineAgent(BaseAgent):
    PHASE_PATTERNS: tuple[PhasePattern, ...] = (
        PhasePattern(
            operator_id="init",
            keywords=("начал", "старт", "запуск", "иници", "импульс", "вход", "trigger", "start", "begin", "init"),
            markers=("init", "entry", "impulse"),
        ),
        PhasePattern(
            operator_id="stabilize",
            keywords=("стабил", "равновес", "удерж", "фикс", "плато", "steady", "stable", "hold", "equilibrium"),
            markers=("stabilize", "hold", "steady"),
        ),
        PhasePattern(
            operator_id="vectorize",
            keywords=("рост", "усилен", "ускор", "градиент", "сдвиг", "направл", "vector", "shift", "acceler", "increase"),
            markers=("vectorize", "shift", "gradient"),
        ),
        PhasePattern(
            operator_id="commute",
            keywords=("переключ", "смен", "переход", "развил", "коммут", "switch", "toggle", "branch", "transition"),
            markers=("commute", "switch", "transition"),
        ),
        PhasePattern(
            operator_id="convolve",
            keywords=("сложн", "комбин", "смеш", "интегр", "насла", "связыв", "объедин", "combine", "merge", "layer", "integrat"),
            markers=("convolve", "merge", "layer"),
        ),
        PhasePattern(
            operator_id="relax",
            keywords=("спад", "снижен", "релакс", "затух", "сглаж", "ослаб", "decay", "relax", "cool", "dissipat"),
            markers=("relax", "decay", "release"),
        ),
        PhasePattern(
            operator_id="focus",
            keywords=("фокус", "финал", "итог", "сход", "закреп", "кристалл", "focus", "final", "result", "converge"),
            markers=("focus", "final", "converge"),
        ),
    )

    DOMAIN_FACTORS = {
        "generic": 1.0,
        "text": 1.0,
        "code": 0.9,
        "process": 1.0,
        "phonetic": 0.95,
        "affective": 0.95,
        "spectral": 0.9,
    }

    DOMAIN_KEYWORDS = {
        "phonetic": ("formant", "pitch", "harmonic", "spectrum"),
        "spectral": ("frequency", "bandwidth", "resonance", "filter"),
        "affective": ("emotion", "feeling", "mood", "tension", "release"),
        "code": ("function", "loop", "variable", "return", "execute"),
        "process": ("step", "phase", "workflow", "stage", "sequence"),
    }

    def analyze(self, content: str, domain: str = "generic") -> OmegaSequence:
        normalized_content = content.strip()
        chunks = self._segment(normalized_content)
        phase_matches = [self._match_phase(pattern, chunks, domain) for pattern in self.PHASE_PATTERNS]
        palette = [self._build_palette_item(phase_match, index, domain) for index, phase_match in enumerate(phase_matches)]
        return OmegaSequence(
            palette=palette,
            phase_matches=phase_matches,
            recursion_depth=0,
            domain=domain,
        )

    def is_available(self) -> bool:
        return True

    def _segment(self, content: str) -> list[tuple[str, int, int]]:
        if not content:
            return []

        segments: list[tuple[str, int, int]] = []
        for match in re.finditer(r"[^\n.!?]+(?:[.!?]+|$)", content, re.MULTILINE):
            segment = match.group(0).strip()
            if segment:
                segments.append((segment, match.start(), match.end()))
        return segments

    def _match_phase(
        self,
        phase_pattern: PhasePattern,
        chunks: list[tuple[str, int, int]],
        domain: str,
    ) -> PhaseMatch:
        best_match: tuple[str, int | None, int | None, int] | None = None

        for segment, start, end in chunks:
            score = self._keyword_score(segment=segment, keywords=phase_pattern.keywords)
            if score > 0:
                if best_match is None or score > best_match[3]:
                    best_match = (segment, start, end, score)

        if best_match is None:
            return self._synthetic_phase_match(phase_pattern)

        segment, start, end, match_count = best_match
        confidence = self._calculate_confidence(
            markers=phase_pattern.markers,
            context=segment,
            phase_position=self._segment_position(chunks=chunks, start_offset=start),
            expected_position=self._operator_index(phase_pattern.operator_id),
            domain=domain,
            marker_count=match_count,
        )
        synthetic = confidence < MIN_CONFIDENCE_SYNTHETIC
        markers = list(phase_pattern.markers)
        if synthetic:
            markers.append("synthetic_low_confidence")

        operator = next(operator for operator in OPERATORS if operator.internal_id == phase_pattern.operator_id)
        return PhaseMatch(
            operator_id=phase_pattern.operator_id,
            display_symbol=operator.display_symbol,
            source_text=segment,
            start_offset=start,
            end_offset=end,
            confidence=confidence,
            synthetic=synthetic,
            markers=markers,
        )

    def _synthetic_phase_match(self, phase_pattern: PhasePattern) -> PhaseMatch:
        operator = next(operator for operator in OPERATORS if operator.internal_id == phase_pattern.operator_id)
        return PhaseMatch(
            operator_id=phase_pattern.operator_id,
            display_symbol=operator.display_symbol,
            source_text=f"synthetic::{phase_pattern.operator_id}",
            start_offset=None,
            end_offset=None,
            confidence=0.0,
            synthetic=True,
            markers=[*phase_pattern.markers, "synthetic_missing"],
        )

    def _calculate_confidence(
        self,
        markers: tuple[str, ...],
        context: str,
        phase_position: int,
        expected_position: int,
        domain: str,
        marker_count: int,
    ) -> float:
        marker_score = min(max(marker_count, len(markers)) * 0.13, 0.40)

        position_diff = abs(phase_position - expected_position)
        if position_diff == 0:
            position_score = 0.20
        elif position_diff == 1:
            position_score = 0.12
        else:
            position_score = 0.05

        context_lower = context.casefold()
        context_matches = sum(1 for marker in markers if marker.casefold() in context_lower)
        context_score = min(context_matches * 0.10, 0.30)

        domain_score = 0.0
        for keyword in self.DOMAIN_KEYWORDS.get(domain, ()):
            if keyword.casefold() in context_lower:
                domain_score += 0.03
        domain_score = min(domain_score, 0.10)

        domain_factor = self.DOMAIN_FACTORS.get(domain, 1.0)
        total = (marker_score + position_score + context_score + domain_score) * domain_factor
        return round(min(max(total, 0.0), 1.0), 3)

    def _keyword_score(self, segment: str, keywords: tuple[str, ...]) -> int:
        normalized = segment.casefold()
        return sum(normalized.count(keyword.casefold()) for keyword in keywords)

    def _segment_position(
        self,
        chunks: list[tuple[str, int, int]],
        start_offset: int | None,
    ) -> int:
        if start_offset is None or not chunks:
            return 0

        for index, (_, start, _) in enumerate(chunks):
            if start == start_offset:
                return index
        return 0

    def _operator_index(self, operator_id: str) -> int:
        for index, operator in enumerate(OPERATORS):
            if operator.internal_id == operator_id:
                return index
        return 0

    def _build_palette_item(self, phase_match: PhaseMatch, index: int, domain: str) -> PaletteItem:
        operator = OPERATORS[index]
        coordinates = self._generate_coordinates(
            operator_id=phase_match.operator_id,
            confidence=phase_match.confidence,
            domain=domain,
            index=index,
            synthetic=phase_match.synthetic,
            init_coordinates=None,
            markers=tuple(phase_match.markers),
            context=phase_match.source_text,
        )
        return PaletteItem(
            operator_id=phase_match.operator_id,
            symbol=operator.display_symbol,
            value=phase_match.source_text,
            coordinates=coordinates,
            confidence=phase_match.confidence,
            synthetic=phase_match.synthetic,
        )

    def _generate_coordinates(
        self,
        operator_id: str,
        confidence: float,
        domain: str,
        index: int,
        synthetic: bool,
        init_coordinates: Coordinates | None,
        markers: tuple[str, ...],
        context: str,
    ) -> Coordinates:
        operator_bias = {
            "init": {"A": 0.68, "S": 0.38, "T": 0.62, "E": 0.54},
            "stabilize": {"A": 0.46, "S": 0.58, "T": 0.44, "E": 0.42},
            "vectorize": {"A": 0.64, "S": 0.52, "T": 0.72, "E": 0.50},
            "commute": {"A": 0.52, "S": 0.56, "T": 0.60, "E": 0.48},
            "convolve": {"A": 0.58, "S": 0.74, "T": 0.57, "E": 0.58},
            "relax": {"A": 0.34, "S": 0.50, "T": 0.36, "E": 0.32},
            "focus": {"A": 0.48, "S": 0.66, "T": 0.42, "E": 0.60},
        }[operator_id]

        domain_shift = {
            "generic": {"A": 0.0, "S": 0.0, "T": 0.0, "E": 0.0},
            "text": {"A": 0.0, "S": 0.02, "T": 0.01, "E": 0.03},
            "code": {"A": 0.03, "S": 0.05, "T": -0.02, "E": -0.03},
            "process": {"A": 0.01, "S": 0.03, "T": 0.04, "E": -0.01},
            "phonetic": {"A": 0.02, "S": 0.08, "T": 0.00, "E": 0.01},
            "affective": {"A": -0.01, "S": 0.00, "T": 0.02, "E": 0.10},
            "spectral": {"A": 0.00, "S": 0.10, "T": -0.01, "E": 0.00},
        }.get(domain, {"A": 0.0, "S": 0.0, "T": 0.0, "E": 0.0})

        confidence_shift = (confidence - 0.5) * 0.18
        index_shift = (index - 3) * 0.015
        synthetic_penalty = -0.08 if synthetic else 0.0

        if operator_id == "focus" and init_coordinates is not None:
            return self.generate_focus_coordinates(
                init_coords=init_coordinates,
                markers=markers,
                context=context,
            )

        values = {}
        for key, base_value in operator_bias.items():
            value = base_value + domain_shift[key] + confidence_shift + index_shift + synthetic_penalty
            values[key] = round(min(max(value, 0.0), 1.0), 3)

        return Coordinates(**values)

    def generate_focus_coordinates(
        self,
        init_coords: Coordinates,
        markers: tuple[str, ...],
        context: str,
    ) -> Coordinates:
        transformed = {
            "A": init_coords.A * 0.92 + 0.04,
            "S": init_coords.S * 1.08 - 0.04,
            "T": init_coords.T * 0.96 + 0.02,
            "E": init_coords.E * 1.05 - 0.025,
        }

        focus_markers = {"converge", "final", "crystallize", "attractor", "focus"}
        context_lower = context.casefold()
        if any(marker.casefold() in focus_markers for marker in markers) or any(
            token in context_lower for token in focus_markers
        ):
            transformed["S"] += 0.05
            transformed["T"] -= 0.03

        return Coordinates(
            **{
                key: round(min(max(value, 0.0), 1.0), 3)
                for key, value in transformed.items()
            }
        )
