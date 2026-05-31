# Omega Invariants Specification v1.0

## 1. Purpose

`omega-invariants` is an offline-first system for extracting and validating 7-phase Omega structures from unstructured input such as text, code, or process descriptions.

The MVP must:
- accept text, code, or mixed narrative input;
- extract seven phase-aligned structural segments;
- map those segments to Omega operators;
- validate engineering interpretations of axioms `A1-A5`;
- compute stability metrics including `D` and `rho`;
- return a deterministic result without requiring network access;
- visualize and export the result.

Optional layers such as local LLM assistance, desktop packaging, and deeper recursion are deferred until the deterministic core is stable.

## 2. Core Entities

All coordinate values are normalized floats in `[0.0, 1.0]`.

### Coordinates

```python
{
  "A": float,
  "S": float,
  "T": float,
  "E": float
}
```

Dimensions:
- `A`: articulatory or activation axis
- `S`: spectral or structural density axis
- `T`: temporal or transition axis
- `E`: emotive or energetic axis

### OperatorDefinition

```python
{
  "internal_id": str,
  "ascii_key": str,
  "display_symbol": str,
  "label": str,
  "color": str,
  "phase_index": int
}
```

### PhaseMatch

```python
{
  "operator_id": str,
  "display_symbol": str,
  "source_text": str,
  "start_offset": int | None,
  "end_offset": int | None,
  "confidence": float,
  "synthetic": bool,
  "markers": list[str]
}
```

### PaletteItem

```python
{
  "operator_id": str,
  "symbol": str,
  "value": str,
  "coordinates": Coordinates,
  "confidence": float,
  "synthetic": bool
}
```

### OmegaSequence

```python
{
  "palette": list[PaletteItem],  # exactly 7 items
  "phase_matches": list[PhaseMatch],  # exactly 7 items
  "recursion_depth": int,
  "domain": str
}
```

### ValidationReport

```python
{
  "A1_monotonic_path": bool,
  "A2_zero_flux": bool,
  "A3_recurrent_closure": bool,
  "A4_operator_isomorphism": bool,
  "A5_adaptive_density": bool,
  "messages": list[str]
}
```

### OmegaResult

```python
{
  "sequence": list[str],
  "palette": list[PaletteItem],
  "phase_matches": list[PhaseMatch],
  "coordinates": list[Coordinates],
  "D_metric": float,
  "rho_values": list[float],
  "stability_flag": bool,
  "corrections_applied": list[str],
  "validation": ValidationReport
}
```

## 3. Operator Mapping

The system uses a dual-layer representation:
- internal logic uses `internal_id` and `ascii_key`;
- UI and export use `display_symbol`.

| phase_index | internal_id | ascii_key | display_symbol | label | color |
|---|---|---|---|---|---|
| 0 | `init` | `INIT` | `∂₀` | Initiation | `#ff4d4d` |
| 1 | `stabilize` | `STAB` | `≈` | Stabilization | `#8b92a5` |
| 2 | `vectorize` | `VECT` | `↑⃗` | Vectorization | `#f2c94c` |
| 3 | `commute` | `COMM` | `⇄` | Commutation | `#f2994a` |
| 4 | `convolve` | `CONV` | `⊗` | Convolution | `#9b51e0` |
| 5 | `relax` | `RLAX` | `↓` | Relaxation | `#27ae60` |
| 6 | `focus` | `FOCS` | `∞` | Focusing | `#2d9cdb` |

## 4. Constants And Thresholds

```python
LAMBDA = 0.85
SIGMA_THRESHOLD = 0.30
RHO_MIN = 0.40
RHO_MAX = 1.00
D_MAX_ACCEPTABLE = 0.15
D_STABLE_AVG = 0.043
D_STABLE_STD = 0.009
KAPPA = 0.12
ZERO_FLUX_TOLERANCE = 1e-6
A3_EPSILON = 0.15
MAX_CORRECTION_ITERATIONS = 3
MIN_CONFIDENCE_SYNTHETIC = 0.20
```

Coordinate weights:

```python
WEIGHTS = {
  "A": 0.15,
  "S": 0.30,
  "T": 0.25,
  "E": 0.30,
}
```

## 5. Axioms: Engineering Interpretation

### A1. Monotonic Path

Requirements:
- `len(palette) == 7`
- phases must appear in strict fixed order from index `0..6`
- no skips, reversals, duplicates, or branching inside the normalized output sequence

Validation:
- compare `phase_index` sequence against `[0, 1, 2, 3, 4, 5, 6]`

### A2. Zero Flux

Meaning:
- net parameter drift over a full cycle must be normalized to zero or near-zero

Validation:
- for each coordinate axis, compute cumulative deltas across the cycle
- after normalization, require `abs(sum_delta) < ZERO_FLUX_TOLERANCE`

Correction:
- if residual drift exceeds tolerance, redistribute local deltas across adjacent phases before the final evaluation

### A3. Recurrent Closure

Engineering interpretation for MVP:
- terminal coordinates must remain within an epsilon-bounded neighborhood of the initial coordinates

Reference rule:

```python
def validate_A3(initial, terminal, epsilon=0.15):
    return all(
        initial[key] - epsilon <= terminal[key] <= initial[key] + epsilon
        for key in ("A", "S", "T", "E")
    )
```

This is intentionally narrower and more testable than the abstract convex-hull version in the raw draft.

### A4. Operator Isomorphism

Meaning:
- equivalent operator roles should produce structurally comparable transforms across domains

MVP interpretation:
- hold as a comparative test property rather than a hard runtime rule
- compare analogous sequences from different domains and accept if `D <= 0.11`

Status:
- implemented as a validation utility and test fixture target, not as a blocking runtime constraint for the first release

### A5. Adaptive Density

Formula:

```python
rho_n = clip(exp(-LAMBDA * sigma_n**2), RHO_MIN, RHO_MAX)
```

Meaning:
- high stochasticity lowers transition density and increases smoothing

Runtime effect:
- increase overlap duration and smoothing when `sigma > SIGMA_THRESHOLD`
- reduce abrupt phase transitions in noisy inputs

Validation:
- each `rho_n` must stay inside `[RHO_MIN, RHO_MAX]`

## 6. Confidence And Synthetic Markers

`OfflineAgent` is deterministic and must assign `confidence` to each detected phase.

Initial rule:
- `raw_score = min(match_count * 0.15, 1.0)`
- `confidence = raw_score * domain_relevance_factor`
- if `confidence < 0.20`, mark the phase as `synthetic=True`

Synthetic phases:
- explicitly fill missing slots when fewer than 7 reliable phases are found
- must remain visible in API, UI, and export output

## 7. Data Flow

```text
input text/code
  -> segmentation
  -> OfflineAgent extraction
  -> 7 PhaseMatch items
  -> PaletteItem normalization
  -> OmegaEngine validation + metrics
  -> OmegaResult
  -> API response / UI visualization / export
```

## 8. MVP Scope

Included in MVP:
- deterministic `OfflineAgent`
- deterministic `OmegaEngine`
- engineering validations for `A1`, `A2`, `A3`, `A5`
- utility-level validation for `A4`
- backend API with `POST /analyze`
- operator metadata endpoint
- basic React UI for input and result visualization
- JSON and HTML export
- local development without Docker

Explicitly deferred:
- remote APIs
- mandatory LLM dependency
- Docker-based runtime
- PWA packaging
- desktop packaging
- recursion depth greater than `R1`
- advanced multilingual extraction beyond initial RU-first heuristics

## 9. Repository Shape

```text
backend/
  api/
  agents/
  core/
  tests/
frontend/
  src/
scripts/
docs/
```

## 10. Non-Goals For This Stage

- building the full abstract Omega meta-framework from the raw research draft
- solving arbitrary semantic parsing with high recall
- optimizing for production throughput before correctness
- hiding uncertainty from the user

## 11. Definition Of Done For MVP

- project starts locally with backend and frontend as separate processes
- analysis works without internet access
- output always contains a 7-phase normalized sequence
- synthetic and low-confidence results are explicit
- core axioms are test-covered
- result can be exported as JSON and HTML
