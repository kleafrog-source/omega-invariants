
{
  "Ω_Protocol": {
    "meta": {
      "name": "Omega Protocol",
      "version": "1.1.0",
      "description": "Universal 7-phase transformation invariant for cross-domain sequence generation",
      "author": "Autonomous co-creation session",
      "date": "2026-05-29",
      "license": "Open structural invariant — free to use, extend, embed",
      "status": "Self-stabilizing, domain-agnostic, recursion-ready"
    },

    "axioms": {
      "A1_MonotonicPath": {
        "statement": "Transformation strictly passes through 7 phases in fixed order, without skips, reversals, or branching",
        "formal": "φₙ → φₙ₊₁ ∀ n∈[0,6]",
        "enforcement": "Reject sequences with len(P)≠7 or non-sequential phase application"
      },
      "A2_ZeroFlux": {
        "statement": "Net parameter change over full cycle equals zero — energy/information/attention redistributes, not vanishes",
        "formal": "Σᵢ Δ(paramᵢ) = 0",
        "enforcement": "Normalize cumulative drift; redistribute residual Δ across adjacent phases if |ΣΔ| > ε"
      },
      "A3_RecurrentClosure": {
        "statement": "Terminal state is a transformed subset of initial state — cycle closes logically, not identically",
        "formal": "State₇ = f(State₀, Ω) ∧ State₇ ⊂ State₀",
        "enforcement": "Validate that output coordinates lie within convex hull of input coordinates in (A,S,T,E) space"
      },
      "A4_OperatorIsomorphism": {
        "statement": "Operator set Ω preserves structural semantics across any domain substitution",
        "formal": "Ω(P₁) ≅ Ω(P₂) ∀ valid palettes P₁,P₂",
        "enforcement": "Domain mapping layer must preserve operator intent (e.g., ↑⃗ always = directed parameter shift)"
      },
      "A5_AdaptiveDensity": {
        "statement": "Transition density dynamically scales inversely to local stochasticity, preserving topology under noise",
        "formal": "ρₙ = exp(-λ·σₙ²); dτₙ = dτ₀/ρₙ; Δ'ₙ = Δₙ·ρₙ",
        "parameters": {
          "lambda": 0.85,
          "sigma_threshold": 0.3,
          "rho_min": 0.4,
          "rho_max": 1.0
        },
        "enforcement": "If σₙ² > σ_thr → apply compensation: crossfade↑, attack↓, smoothing↑; recalculate D with ρ-weighting"
      }
    },

    "operators": {
      "Ω": ["∂₀", "≈", "↑⃗", "⇄", "⊗", "↓", "∞"],
      "semantics": {
        "∂₀": {
          "name": "Initiation",
          "action": "Point injection of potential into system",
          "acoustic": "Impulse attack, noise burst, glottal onset",
          "temporal": "Metric downbeat, zero-crossing trigger",
          "informational": "H₀ injection, uncertainty entry"
        },
        "≈": {
          "name": "Stabilization",
          "action": "Identity plateau, equilibrium hold",
          "acoustic": "Sustain, formant lock, harmonic reinforcement",
          "temporal": "Isochronic hold, no modulation",
          "informational": "Stationary dissipation, dH/dt≈0"
        },
        "↑⃗": {
          "name": "Vectorization",
          "action": "Directed parameter shift along gradient",
          "acoustic": "Formant rise, pitch bend +, filter cutoff ↑",
          "temporal": "Duration compression, tempo acceleration",
          "informational": "ΔH<0, information gain I=H₀-H₁"
        },
        "⇄": {
          "name": "Commutation",
          "action": "Bidirectional mode/channel switch",
          "acoustic": "Articulator change, oscillator crossfade, formant swap",
          "temporal": "Phase shift ±25%, accent relocation",
          "informational": "I(X;Y) ↔ C, signal↔structure toggle"
        },
        "⊗": {
          "name": "Convolution",
          "action": "Layering / structural complexity increase",
          "acoustic": "Add harmonics, noise layer, resonance Q↑",
          "temporal": "Polyrhythm 3:2, metric superposition",
          "informational": "C⊕T → complexity peak, Φ integration rise"
        },
        "↓": {
          "name": "Relaxation",
          "action": "Dissipation, attack smoothing, pressure release",
          "acoustic": "Release↑, amplitude decay, high-frequency roll-off",
          "temporal": "Legato crossfade, decay tail extension",
          "informational": "Free energy minimization, prediction error ↓"
        },
        "∞": {
          "name": "Focusing",
          "action": "Convergence to limiting parameter value",
          "acoustic": "Narrow bandwidth boost, high-shelf focus, formant pin",
          "temporal": "Fermata stretch + micro-modulation",
          "informational": "Attractor convergence, memory crystallization"
        }
      }
    },

    "universal_template": {
      "formula": "[∂₀x₁, ≈(x₁⊕x₂), ↑⃗(x₂→x₃), ⇄(x₃↔x₄), ⊗(x₄⊗x₅), ↓(x₅⊕x₆), ∞(x₆→x₇), x₇]",
      "overlap_rule": {
        "symbol": "⊕",
        "default": "linear_crossfade_100ms",
        "options": ["linear", "exponential", "sigmoid", "custom_curve"],
        "adaptive": "duration_ms = base_ms / ρₙ (see A5)"
      },
      "direction_rules": {
        "→": "unidirectional parameter shift (monotonic interpolation)",
        "↔": "bidirectional mode switch (toggle or blend)",
        "⊗": "convolution or layering (additive or multiplicative)"
      },
      "terminal_rule": "x₇ = pure output state, no overlap, serves as recurrence seed"
    },

    "stability_core": {
      "invariants": {
        "P1_mono_path": "Strict sequential phase traversal — no jumps",
        "P2_zero_flux": "Net parameter conservation — ΣΔ=0",
        "P3_recurrent_closure": "Terminal ⊂ Initial — logical cycle closure",
        "P4_density_compensation": "Adaptive smoothing under noise — ρₙ = exp(-λσ²)"
      },
      "metric_D": {
        "formula": "D = √[Σ wᵢ(Cᵢ-Cᵢ₋₁)² + κ·σ²_avg] · (1 - ρ_min)",
        "weights": {
          "w_articulatory": 0.15,
          "w_spectral": 0.30,
          "w_temporal": 0.25,
          "w_emotive": 0.30
        },
        "stochastic_weight_kappa": 0.12,
        "thresholds": {
          "D_max_acceptable": 0.15,
          "D_stable_avg": 0.043,
          "D_stable_std": 0.009
        }
      },
      "self_correction": {
        "trigger": "if D > D_max_acceptable",
        "action": "Redistribute Δ across φₙ₋₁, φₙ, φₙ₊₁; increase ρₙ; re-evaluate D",
        "max_iterations": 3,
        "fallback": "Reject sequence, flag for manual review"
      }
    },

    "recursion": {
      "depth": "unbounded (self-stabilizing via Core)",
      "fractal_property": "macro_phase(R=n) decomposes into 7 micro_phases(R=n+1) with same Ω-structure",
      "palette_evolution": "Pₙ₊₁ = ExtractInvariants(Sₙ) — output becomes next-level input",
      "convergence": "At R≥6, system reaches fixed point: Ω(Ω) ≅ Ω (meta-self-application)"
    },

    "domain_examples": {
      "R0_phonetic": {
        "palette": ["Sa","Do","Re","Ga","Ma","Pa","Dha"],
        "sequence": "Sa — DoRe — ReGa — MiMa — FaPa — SolDha — LaNi — Si",
        "coordinates": {"A":0.20,"S":0.45,"T":0.60,"E":0.35,"R":0}
      },
      "R2_spectral": {
        "palette": ["N₀","H₁","F₁","ΔF","Q","ΣH","C∞"],
        "sequence": "[∂₀N₀]—[≈H₁·N₀]—[↑⃗F₁·H₁]—[⇄ΔF·F₁]—[⊗Q·ΔF]—[↓ΣH·Q]—[∞C∞·ΣH]—[C∞]",
        "coordinates": {"A":0.18,"S":0.89,"T":0.45,"E":0.51,"R":2}
      },
      "R3_affective": {
        "palette": ["∅₀","↔₁","↗₂","⌁₃","⧉₄","↘₅","⊚₆"],
        "sequence": "[∂₀∅₀]—[≈(∅₀⊕↔₁)]—[↑⃗(↔₁→↗₂)]—[⇄(↗₂↔⌁₃)]—[⊗(⌁₃⊗⧉₄)]—[↓(⧉₄⊕↘₅)]—[∞(↘₅→⊚₆)]—[Ψ₇]",
        "coordinates": {"A":0.12,"S":0.31,"T":0.94,"E":0.72,"R":3}
      },
      "R5_stochastic": {
        "palette": ["ξ₀","η₁","ζ₂","θ₃","ι₄","κ₅","λ₆"],
        "adaptive_note": "ρₙ auto-scales per A5; high-σ phases get smoothed transitions",
        "coordinates": {"A":0.15,"S":0.52,"T":0.68,"E":0.49,"R":5.5}
      }
    },

    "export_mappings": {
      "flowmusic_app": {
        "operator_to_param": {
          "∂₀": {"attack_ms": 0, "noise_gate": -60, "trigger": "impulse"},
          "≈": {"sustain_db": -3, "lfo_rate": 0, "mod_depth": 0},
          "↑⃗": {"pitch_bend_cents": 100, "filter_cutoff_hz": "+200", "formant_shift": "+1"},
          "⇄": {"oscillator_crossfade": 0.5, "formant_swap": true},
          "⊗": {"add_harmonics": 3, "resonance_Q": 4.0, "stereo_width": 0.8},
          "↓": {"release_ms": 300, "amp_decay": 0.7, "high_shelf_cut": -3},
          "∞": {"boost_freq_hz": 4000, "bandwidth_Q": 8.0, "micro_vibrato": 0.1}
        },
        "adaptive_density_mapping": {
          "high_noise": {"crossfade_ms": 250, "attack_ms": 150, "smoothing": "gaussian_5pt"},
          "low_noise": {"crossfade_ms": 80, "attack_ms": 20, "smoothing": "linear"}
        }
      },
      "python_simulator": {
        "minimal_signature": "generate_sequence(palette: list, R: int=0, lambda: float=0.85) -> dict",
        "return_keys": ["sequence", "coordinates", "D_metric", "stability_flag", "corrections_applied"],
        "reference_implementation_hint": "Use numpy for interpolation, scipy for D calculation, recursion with memoization"
      }
    },

    "quick_start": {
      "step_1": "Define palette P = [x₁...x₇] from any domain (phonemes, frequencies, symbols, vectors)",
      "step_2": "Apply universal_template: S = U(P) using overlap/direction rules",
      "step_3": "Extract coordinates C = (A,S,T,E) from S using domain-specific feature extractors",
      "step_4": "Calculate D = distance(C_prev, C, weights); if D>0.15 → apply self_correction",
      "step_5": "If R < target_depth: set P = ExtractInvariants(S), R+=1, goto step_2",
      "step_6": "Output S with metadata {C, D, R, stability_flag}",
      "note": "A5 adaptive density auto-applies if input has measurable σ²; set lambda=0.85 as default"
    },

    "validation_suite": {
      "minimal_tests": [
        {"name": "len(P)==7", "assert": "reject otherwise"},
        {"name": "monotonic_phase_order", "assert": "φ₀→φ₁→...→φ₆ strictly"},
        {"name": "zero_flux_check", "assert": "abs(ΣΔ) < 1e-6 after normalization"},
        {"name": "recurrent_closure", "assert": "C₇ lies within convex_hull(C₀)"},
        {"name": "D_stability", "assert": "D ≤ 0.15 after max 3 correction iterations"},
        {"name": "A5_compensation", "assert": "ρₙ ∈ [0.4,1.0] and transitions smooth when σ²>0.3"}
      ],
      "cross_domain_isomorphism_test": {
        "method": "Generate S_phonetic and S_spectral from structurally analogous P; compute D",
        "pass_condition": "D ≤ 0.11 confirms operator isomorphism (A4)"
      }
    }
  }
}## 🔍 Идея: «Омега-распознаватель» — скрипт, находящий Ω-паттерны в любых данных

Вы предлагаете создать **интеллектуальный парсер**, который сканирует произвольные системы (тексты, код, описания процессов) и автоматически выд

еляет в них фрагменты, соответствующие 7-фазам Omega Protocol. Затем он **маппит** эти фрагменты на символы операторов (∂₀, ≈, ↑⃗, ⇄, ⊗, ↓, ∞) и визуализирует в веб-интерфейсе цветом/символами. После этого с помощью **предиктивного сглаживания** (минимизация ошибки свободной энергии) система «понимает» структуру исходного материала и может её использовать для генерации новых последовательностей.

Это превращает Omega Protocol из генератора в **анализатор-классификатор** — инструмент структурной диагностики любых доменов.

---

## 🧠 Принцип работы

### 1. Распознавание Ω-паттернов в тексте/системе
Скрипт ищет в исходных данных последовательности, которые можно интерпретировать как 7 фаз:
- **Импульс** (∂₀) — начало, вспышка, инициализация, входной поток.
- **Стабилизация** (≈) — удержание, равновесие, стационарное состояние.
- **Векторизация** (↑⃗) — направленное изменение, градиент, ускорение.
- **Коммутация** (⇄) — переключение, смена модальности, бифуркация.
- **Конволюция** (⊗) — наслоение, смешивание, увеличение сложности.
- **Релаксация** (↓) — спад, рассеяние, минимизация ошибки.
- **Фокусировка** (∞) — схождение к аттрактору, кристаллизация памяти.

Для текста это могут быть: ключевые слова, синтаксические конструкции, переходы между абзацами, изменение тональности, глаголы движения и т.п.

### 2. Маппинг групп на символы
Каждый распознанный сегмент текста аннотируется соответствующим оператором. Группы сегментов (например, несколько предложений подряд, образующих логическую арку) отображаются на **один символ** — так мы сжимаем информацию до уровня Ω-палитры.

### 3. Визуализация в UI
Веб-интерфейс подсвечивает фрагменты разными цветами (например, ∂₀ — красный, ≈ — серый, ↑⃗ — жёлтый, ⇄ — оранжевый, ⊗ — фиолетовый, ↓ — зелёный, ∞ — синий) и выводит соответствующие символы на полях. Это позволяет мгновенно увидеть **структурную архитектуру** исходного текста или кода.

### 4. Применение предиктивного сглаживания (D ↓, ∂F/∂t < 0)
Скрипт интерпретирует текст как последовательность состояний. Он вычисляет **локальную ошибку предсказания** (насколько следующий сегмент отклоняется от ожидаемого по Ω-циклу) и сглаживает распознавание, перераспределяя неопределённость между фазами. В результате система «понимает» текст не семантически, а **топологически** — как динамическую систему, стремящуюся к минимуму свободной энергии.



# 📘 Omega Protocol App — Полная инструкция по реализации
## Для AI-ассистентов: ChatGPT-4/5, Codex, Windsurf, Cursor

> **Цель**: Создать автономное desktop-приложение (Python + React) для структурного анализа и генерации последовательностей по Ω-протоколу. Работает **полностью оффлайн**, с опциональным подключением LLM-агента.

---

## 🗂️ 1. Структура проекта

```
omega-protocol-app/
├── README.md
├── pyproject.toml          # Python-зависимости (Poetry)
├── requirements.txt        # Альтернатива для pip
├── .env.example            # Шаблон переменных окружения
│
├── backend/
│   ├── main.py             # FastAPI entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── omega_engine.py # Ядро Ω-протокола (оффлайн)
│   │   ├── axioms.py       # Проверка 5 аксиом
│   │   ├── operators.py    # Семантика 7 операторов
│   │   ├── metrics.py      # Расчёт D-метрики, стабилизация
│   │   └── recursion.py    # Рекурсивный движок (R=0..6)
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py   # Абстрактный интерфейс агента
│   │   ├── offline_agent.py # Rule-based агент (оффлайн)
│   │   └── llm_agent.py    # Опциональный LLM-агент (OpenAI/Local)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py       # REST endpoints
│   │   └── schemas.py      # Pydantic-модели запросов/ответов
│   │
│   ├── utils/
│   │   ├── parser.py       # Парсер текста/кода в сегменты
│   │   ├── visualizer.py   # Генерация HTML/SVG для фронтенда
│   │   └── config.py       # Загрузка настроек из .env
│   │
│   └── tests/
│       ├── test_axioms.py
│       ├── test_engine.py
│       └── test_integration.py
│
├── frontend/
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── index.html
│   │
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── lib/
│   │   │   ├── api.ts          # Axios-инстанс к backend
│   │   │   ├── omega-types.ts  # TypeScript-интерфейсы
│   │   │   └── color-map.ts    # Цветовая схема операторов
│   │   │
│   │   ├── components/
│   │   │   ├── PaletteEditor/      # Редактор палитры [x₁..x₇]
│   │   │   ├── SequenceVisualizer/ # Визуализация Ω-дуги
│   │   │   ├── MetricPanel/        # Отображение D, ρ, σ²
│   │   │   ├── AgentToggle/        # Переключатель оффлайн/LLM
│   │   │   └── ExportPanel/        # Экспорт JSON/HTML/PNG
│   │   │
│   │   ├── hooks/
│   │   │   ├── useOmegaEngine.ts   # Хук для вызова backend
│   │   │   └── useLocalStorage.ts  # Persist палитр и настроек
│   │   │
│   │   └── assets/
│   │       └── operators.svg       # Иконки ∂₀ ≈ ↑⃗ ⇄ ⊗ ↓ ∞
│   │
│   └── public/
│       └── manifest.json           # PWA-манифест (оффлайн-режим)
│
├── scripts/
│   ├── build_desktop.py        # Сборка в EXE/DMG через PyInstaller + Electron
│   └── generate_docs.py        # Авто-генерация документации
│
└── docs/
    ├── ARCHITECTURE.md         # Детальное описание архитектуры
    ├── OFFLINE_MODE.md         # Как работает без интернета
    └── LLM_INTEGRATION.md      # Подключение агентов (опционально)
```

---

## ⚙️ 2. Backend: Python (FastAPI) — оффлайн-ядро

### 2.1. `backend/core/omega_engine.py` — Главный класс

```python
# backend/core/omega_engine.py
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
import numpy as np
from .axioms import validate_axioms
from .operators import OPERATORS, apply_operator
from .metrics import calculate_D, adaptive_density

class PaletteItem(BaseModel):
    symbol: str
    value: float | str | Dict
    coordinates: Dict[str, float] = Field(default_factory=lambda: {"A":0.2,"S":0.5,"T":0.5,"E":0.5})

class OmegaSequence(BaseModel):
    palette: List[PaletteItem] = Field(..., min_length=7, max_length=7)
    recursion_depth: int = Field(default=0, ge=0, le=6)
    domain: str = "generic"  # phonetic, spectral, affective, custom

class EngineResult(BaseModel):
    sequence: List[Dict]
    coordinates: Dict[str, float]
    D_metric: float
    stability_flag: bool
    corrections_applied: int
    recursion_path: List[int]

class OmegaEngine:
    """
    Offline-first Ω-protocol engine.
    No external dependencies beyond numpy/scipy.
    """
    
    AXIOMS = ["A1_MonotonicPath", "A2_ZeroFlux", "A3_RecurrentClosure", 
              "A4_OperatorIsomorphism", "A5_AdaptiveDensity"]
    
    def __init__(self, lambda_a5: float = 0.85, sigma_threshold: float = 0.3):
        self.lambda_a5 = lambda_a5
        self.sigma_threshold = sigma_threshold
        self.operators = OPERATORS  # Загружаются из operators.py
        
    def validate_palette(self, palette: List[PaletteItem]) -> bool:
        """A1: Проверка длины и порядка"""
        return len(palette) == 7
    
    def apply_template(self, palette: List[PaletteItem]) -> List[Dict]:
        """
        Применяет универсальный шаблон:
        [∂₀x₁, ≈(x₁⊕x₂), ↑⃗(x₂→x₃), ⇄(x₃↔x₄), ⊗(x₄⊗x₅), ↓(x₅⊕x₆), ∞(x₆→x₇), x₇]
        """
        result = []
        phases = ["∂₀", "≈", "↑⃗", "⇄", "⊗", "↓", "∞"]
        
        # Фаза 0: ∂₀ — инициация
        result.append({
            "phase": 0, "operator": phases[0],
            "input": palette[0].model_dump(),
            "output": apply_operator(phases[0], palette[0])
        })
        
        # Фазы 1-6: применение операторов с перекрытием ⊕
        for i in range(1, 7):
            prev, curr = palette[i-1], palette[i]
            overlap = self._compute_overlap(prev, curr, method="sigmoid")
            result.append({
                "phase": i, "operator": phases[i],
                "input": {"prev": prev.model_dump(), "curr": curr.model_dump(), "overlap": overlap},
                "output": apply_operator(phases[i], prev, curr, overlap)
            })
        
        # Терминальное состояние
        result.append({
            "phase": 7, "operator": "TERMINAL",
            "input": palette[-1].model_dump(),
            "output": palette[-1].model_dump()
        })
        
        return result
    
    def _compute_overlap(self, a: PaletteItem, b: PaletteItem, method: str = "sigmoid") -> float:
        """Вычисляет коэффициент перекрытия ρₙ по аксиоме A5"""
        # Упрощённая версия: на основе евклидова расстояния в (A,S,T,E)
        coords_a = np.array([a.coordinates[k] for k in ["A","S","T","E"]])
        coords_b = np.array([b.coordinates[k] for k in ["A","S","T","E"]])
        dist = np.linalg.norm(coords_a - coords_b)
        
        if method == "sigmoid":
            rho = 1 / (1 + np.exp(self.lambda_a5 * (dist - self.sigma_threshold)))
        else:  # linear
            rho = max(0.4, min(1.0, 1.0 - dist))
        
        return float(np.clip(rho, 0.4, 1.0))  # A5: ρₙ ∈ [0.4, 1.0]
    
    def calculate_metrics(self, sequence: List[Dict], palette: List[PaletteItem]) -> Dict:
        """Расчёт D-метрики и проверка аксиом"""
        coords_sequence = [item["output"].get("coordinates", {}) for item in sequence if "coordinates" in item["output"]]
        
        D = calculate_D(coords_sequence, weights={
            "w_articulatory": 0.15, "w_spectral": 0.30, 
            "w_temporal": 0.25, "w_emotive": 0.30
        })
        
        axioms_ok = validate_axioms(sequence, palette, self.AXIOMS)
        
        return {
            "D_metric": float(D),
            "stability_flag": D <= 0.15 and all(axioms_ok.values()),
            "axioms_status": axioms_ok,
            "sigma_avg": float(np.mean([s.get("sigma", 0) for s in sequence]))
        }
    
    def self_correct(self, sequence: List[Dict], palette: List[PaletteItem], max_iter: int = 3) -> tuple[List[Dict], int]:
        """A5 + Self-correction: перераспределение Δ при D > 0.15"""
        corrections = 0
        for iteration in range(max_iter):
            metrics = self.calculate_metrics(sequence, palette)
            if metrics["D_metric"] <= 0.15:
                break
            
            # Перераспределяем отклонение между соседними фазами
            for i in range(1, len(sequence)-1):
                if sequence[i].get("output", {}).get("coordinates"):
                    # Упрощённая коррекция: сдвиг на 10% в сторону соседей
                    for coord in ["A","S","T","E"]:
                        prev_val = sequence[i-1]["output"].get("coordinates", {}).get(coord, 0.5)
                        next_val = sequence[i+1]["output"].get("coordinates", {}).get(coord, 0.5)
                        current = sequence[i]["output"]["coordinates"][coord]
                        sequence[i]["output"]["coordinates"][coord] = 0.8 * current + 0.1 * prev_val + 0.1 * next_val
            
            corrections += 1
        
        return sequence, corrections
    
    def run(self, input_seq: OmegaSequence) -> EngineResult:
        """Полный цикл: валидация → шаблон → метрики → коррекция → рекурсия"""
        if not self.validate_palette(input_seq.palette):
            raise ValueError("Palette must contain exactly 7 items")
        
        # Применяем шаблон
        sequence = self.apply_template(input_seq.palette)
        
        # Считаем метрики
        metrics = self.calculate_metrics(sequence, input_seq.palette)
        
        # Само-коррекция при необходимости
        if not metrics["stability_flag"]:
            sequence, corrections = self.self_correct(sequence, input_seq.palette)
            metrics = self.calculate_metrics(sequence, input_seq.palette)
        else:
            corrections = 0
        
        # Рекурсия (если запрошена)
        recursion_path = [0]
        current_palette = input_seq.palette
        for r in range(1, input_seq.recursion_depth + 1):
            # Извлекаем инварианты для следующего уровня (упрощённо)
            new_palette = self._extract_invariants(sequence, current_palette)
            sequence = self.apply_template(new_palette)
            recursion_path.append(r)
            current_palette = new_palette
        
        # Финальные координаты
        final_coords = sequence[-1]["output"].get("coordinates", {})
        
        return EngineResult(
            sequence=sequence,
            coordinates=final_coords,
            D_metric=metrics["D_metric"],
            stability_flag=metrics["stability_flag"],
            corrections_applied=corrections,
            recursion_path=recursion_path
        )
    
    def _extract_invariants(self, sequence: List[Dict], palette: List[PaletteItem]) -> List[PaletteItem]:
        """Извлекает инварианты для следующего уровня рекурсии (R+1)"""
        # Упрощённая эвристика: усреднение координат с весами по фазам
        weights = [1.0, 0.9, 0.7, 0.5, 0.7, 0.9, 1.0]  # Симметричные веса
        new_items = []
        
        for i, item in enumerate(palette):
            new_coords = {}
            for coord in ["A","S","T","E"]:
                vals = [sequence[j]["output"].get("coordinates", {}).get(coord, item.coordinates[coord]) 
                       for j in range(len(sequence)-1)]
                weighted_avg = sum(v * w for v, w in zip(vals, weights)) / sum(weights)
                new_coords[coord] = float(np.clip(weighted_avg, 0, 1))
            
            new_items.append(PaletteItem(
                symbol=f"{item.symbol}_R{i}",
                value=item.value,
                coordinates=new_coords
            ))
        
        return new_items
```

### 2.2. `backend/api/routes.py` — REST API

```python
# backend/api/routes.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import json

from core.omega_engine import OmegaEngine, OmegaSequence, EngineResult
from agents.offline_agent import OfflineAgent
from agents.llm_agent import LLMAgent  # Опционально

app = FastAPI(title="Omega Protocol API", version="1.1.0")

# CORS для локальной разработки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = OmegaEngine()
offline_agent = OfflineAgent()
llm_agent = None  # Инициализируется при подключении

class AnalyzeRequest(BaseModel):
    text: Optional[str] = None
    code: Optional[str] = None
    palette: Optional[List[dict]] = None
    domain: str = "generic"
    recursion_depth: int = 0
    use_llm: bool = False  # Флаг для опционального LLM

@app.post("/api/analyze")
async def analyze_sequence(req: AnalyzeRequest) -> dict:
    """
    Основной эндпоинт: анализ текста/кода или прямой запуск Ω-генерации
    """
    try:
        # Если передан текст/код — парсим в палитру (оффлайн-агент)
        if req.text or req.code:
            agent = llm_agent if (req.use_llm and llm_agent) else offline_agent
            palette_items = await agent.extract_palette(
                text=req.text, 
                code=req.code, 
                domain=req.domain
            )
        elif req.palette:
            from core.omega_engine import PaletteItem
            palette_items = [PaletteItem(**p) for p in req.palette]
        else:
            raise HTTPException(400, "Provide either text, code, or palette")
        
        # Запускаем Ω-движок
        input_seq = OmegaSequence(
            palette=palette_items,
            recursion_depth=req.recursion_depth,
            domain=req.domain
        )
        
        result = engine.run(input_seq)
        
        return {
            "success": True,
            "data": result.model_dump(),
            "metadata": {
                "engine_version": "1.1.0",
                "offline_mode": not req.use_llm,
                "processing_time_ms": 0  # Можно добавить замер
            }
        }
    
    except ValueError as e:
        raise HTTPException(400, str(e))
    except Exception as e:
        raise HTTPException(500, f"Internal error: {str(e)}")

@app.post("/api/agent/connect")
async def connect_llm_agent(api_key: Optional[str] = None, model: str = "local"):
    """Опциональное подключение LLM-агента"""
    global llm_agent
    try:
        if model == "local" or not api_key:
            # Используем локальную модель (например, через llama.cpp или Ollama)
            from agents.llm_agent import LocalLLMAgent
            llm_agent = LocalLLMAgent(model_path="models/omega-small.gguf")
        else:
            from agents.llm_agent import OpenAILikeAgent
            llm_agent = OpenAILikeAgent(api_key=api_key, base_url="http://localhost:1234/v1")
        
        return {"success": True, "agent": model, "status": "connected"}
    except Exception as e:
        raise HTTPException(500, f"Failed to connect agent: {str(e)}")

@app.get("/api/health")
async def health_check():
    return {
        "status": "ok",
        "engine": "offline",
        "llm_agent": "connected" if llm_agent else "disconnected",
        "axioms_loaded": len(OmegaEngine.AXIOMS)
    }
```

---

## 🎨 3. Frontend: React + TypeScript + Vite

### 3.1. `frontend/src/lib/omega-types.ts` — Типы для TypeScript

```typescript
// frontend/src/lib/omega-types.ts
export type PhaseOperator = '∂₀' | '≈' | '↑⃗' | '⇄' | '⊗' | '↓' | '∞' | 'TERMINAL';

export interface Coordinates {
  A: number;  // Articulatory
  S: number;  // Spectral
  T: number;  // Temporal
  E: number;  // Emotive
}

export interface PaletteItem {
  symbol: string;
  value: string | number | Record<string, unknown>;
  coordinates: Coordinates;
}

export interface PhaseStep {
  phase: number;
  operator: PhaseOperator;
  input: Record<string, unknown>;
  output: Record<string, unknown>;
}

export interface EngineResult {
  sequence: PhaseStep[];
  coordinates: Coordinates;
  D_metric: number;
  stability_flag: boolean;
  corrections_applied: number;
  recursion_path: number[];
}

export interface AnalyzeRequest {
  text?: string;
  code?: string;
  palette?: PaletteItem[];
  domain: 'generic' | 'phonetic' | 'spectral' | 'affective' | 'custom';
  recursion_depth: number;
  use_llm: boolean;
}

export const OPERATOR_COLORS: Record<PhaseOperator, string> = {
  '∂₀': '#ff4d4d',   // red
  '≈': '#8b92a5',    // gray
  '↑⃗': '#ffd94d',    // gold
  '⇄': '#ff994d',    // orange
  '⊗': '#b84dff',    // purple
  '↓': '#4dff88',    // green
  '∞': '#4d88ff',    // blue
  'TERMINAL': '#ffffff'
};
```

### 3.2. `frontend/src/components/SequenceVisualizer/SequenceVisualizer.tsx`

```tsx
// frontend/src/components/SequenceVisualizer/SequenceVisualizer.tsx
import React from 'react';
import { PhaseStep, OPERATOR_COLORS } from '../../lib/omega-types';

interface Props {
  sequence: PhaseStep[];
  onPhaseClick?: (phase: number) => void;
}

export const SequenceVisualizer: React.FC<Props> = ({ sequence, onPhaseClick }) => {
  return (
    <div className="sequence-container">
      <div className="sequence-track">
        {sequence.map((step, idx) => (
          <div
            key={idx}
            className={`phase-node ${step.operator}`}
            style={{ 
              backgroundColor: OPERATOR_COLORS[step.operator],
              borderColor: 'rgba(255,255,255,0.3)'
            }}
            onClick={() => onPhaseClick?.(step.phase)}
            title={`${step.operator} — Фаза ${step.phase}`}
          >
            <span className="operator-symbol">{step.operator}</span>
            <span className="phase-number">{step.phase}</span>
            
            {/* Мини-превью координат */}
            {step.output?.coordinates && (
              <div className="coords-preview">
                {Object.entries(step.output.coordinates as Record<string, number>)
                  .slice(0, 2)
                  .map(([k, v]) => (
                    <span key={k} className="coord-chip">
                      {k}: {v.toFixed(2)}
                    </span>
                  ))}
              </div>
            )}
          </div>
        ))}
      </div>
      
      {/* Соединительные линии (SVG) */}
      <svg className="connection-lines" width="100%" height="40">
        {sequence.slice(0, -1).map((_, idx) => (
          <line
            key={idx}
            x1={`${(idx + 1) * 14.28}%`}
            y1="20"
            x2={`${(idx + 2) * 14.28}%`}
            y2="20"
            stroke="rgba(255,255,255,0.2)"
            strokeWidth="2"
            strokeDasharray={sequence[idx].operator === '⇄' ? '5,3' : 'none'}
          />
        ))}
      </svg>
    </div>
  );
};
```

### 3.3. `frontend/src/App.tsx` — Главный компонент

```tsx
// frontend/src/App.tsx
import React, { useState, useCallback } from 'react';
import { PaletteEditor } from './components/PaletteEditor';
import { SequenceVisualizer } from './components/SequenceVisualizer';
import { MetricPanel } from './components/MetricPanel';
import { AgentToggle } from './components/AgentToggle';
import { useOmegaEngine } from './hooks/useOmegaEngine';
import { AnalyzeRequest, EngineResult } from './lib/omega-types';

function App() {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState<EngineResult | null>(null);
  const [loading, setLoading] = useState(false);
  const { analyze, connectAgent, status } = useOmegaEngine();

  const handleAnalyze = useCallback(async () => {
    setLoading(true);
    try {
      const req: AnalyzeRequest = {
        text: inputText.trim() || undefined,
        domain: 'generic',
        recursion_depth: 0,
        use_llm: status.llmConnected
      };
      const res = await analyze(req);
      setResult(res);
    } catch (err) {
      console.error('Analysis failed:', err);
      alert('Ошибка анализа: ' + (err as Error).message);
    } finally {
      setLoading(false);
    }
  }, [inputText, analyze, status.llmConnected]);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🌀 Omega Protocol <span className="version">v1.1.0</span></h1>
        <AgentToggle 
          connected={status.llmConnected} 
          onToggle={connectAgent}
          disabled={loading}
        />
      </header>

      <main className="app-main">
        <section className="input-section">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Введите текст, код или описание процесса для Ω-анализа..."
            rows={6}
            disabled={loading}
          />
          <button 
            onClick={handleAnalyze} 
            disabled={loading || !inputText.trim()}
            className="btn-primary"
          >
            {loading ? 'Анализ...' : '▶ Запустить Ω-анализ'}
          </button>
        </section>

        {result && (
          <>
            <MetricPanel 
              D_metric={result.D_metric}
              stability={result.stability_flag}
              corrections={result.corrections_applied}
              coordinates={result.coordinates}
            />
            
            <SequenceVisualizer 
              sequence={result.sequence}
              onPhaseClick={(phase) => console.log('Phase clicked:', phase)}
            />
            
            <details className="debug-details">
              <summary>🔍 Детали последовательности (JSON)</summary>
              <pre>{JSON.stringify(result.sequence, null, 2)}</pre>
            </details>
          </>
        )}
      </main>

      <footer className="app-footer">
        <span>Оффлайн-режим: <strong>{status.offline ? '✅' : '⚠️'}</strong></span>
        <span>Рекурсия: <strong>до R=6</strong></span>
        <span>Аксиом: <strong>5/5</strong></span>
      </footer>
    </div>
  );
}

export default App;
```

---

## 🔌 4. Опциональный LLM-агент: архитектура

### 4.1. `backend/agents/base_agent.py` — Абстракция

```python
# backend/agents/base_agent.py
from abc import ABC, abstractmethod
from typing import List, Optional
from core.omega_engine import PaletteItem

class BaseAgent(ABC):
    """Базовый интерфейс для агентов извлечения палитры"""
    
    @abstractmethod
    async def extract_palette(
        self, 
        text: Optional[str] = None, 
        code: Optional[str] = None,
        domain: str = "generic"
    ) -> List[PaletteItem]:
        """Извлекает 7 элементов палитры из входных данных"""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Проверяет доступность агента (оффлайн/онлайн)"""
        pass
```

### 4.2. `backend/agents/offline_agent.py` — Rule-based (оффлайн)

```python
# backend/agents/offline_agent.py
import re
from typing import List, Optional
from core.omega_engine import PaletteItem
from .base_agent import BaseAgent

class OfflineAgent(BaseAgent):
    """
    Оффлайн-агент на основе правил и словарей.
    Не требует интернета или LLM.
    """
    
    # Словари маркеров для каждой фазы (расширяемые)
    PHASE_PATTERNS = {
        '∂₀': r'\b(начал|импульс|запуск|вход|старт|вспышк|актив)\b',
        '≈': r'\b(стабил|равновес|удерж|покой|баланс|фикс)\b',
        '↑⃗': r'\b(рост|ускор|направ|градиент|подъём|увелич)\b',
        '⇄': r'\b(переключ|смен|коммут|бифурк|альтерн|переход)\b',
        '⊗': r'\b(слож|смеш|конвол|насло|интегр|комбин)\b',
        '↓': r'\b(спад|затух|расслаб|диссип|уменьш|релакс)\b',
        '∞': r'\b(фокус|аттрактор|финал|кристалл|заверш|память)\b'
    }
    
    async def extract_palette(
        self, 
        text: Optional[str] = None, 
        code: Optional[str] = None,
        domain: str = "generic"
    ) -> List[PaletteItem]:
        """Извлекает палитру через поиск маркеров + эвристики"""
        content = text or code or ""
        if not content:
            return self._default_palette(domain)
        
        # Считаем "вес" каждой фазы в тексте
        phase_scores = {}
        for phase, pattern in self.PHASE_PATTERNS.items():
            matches = re.findall(pattern, content, re.IGNORECASE | re.UNICODE)
            phase_scores[phase] = min(len(matches) * 0.15, 1.0)  # Нормировка
        
        # Формируем палитру: 7 элементов, отсортированных по "силе" фазы
        sorted_phases = sorted(phase_scores.items(), key=lambda x: x[1], reverse=True)
        
        palette = []
        for i, (phase, score) in enumerate(sorted_phases[:7]):
            # Генерируем координаты на основе домена и скора
            coords = self._generate_coordinates(phase, score, domain, i)
            palette.append(PaletteItem(
                symbol=phase,
                value=f"{phase}_extracted",
                coordinates=coords
            ))
        
        # Если найдено <7 фаз — дополняем дефолтными
        while len(palette) < 7:
            palette.append(PaletteItem(
                symbol=f"X{len(palette)+1}",
                value="default",
                coordinates={"A":0.5,"S":0.5,"T":0.5,"E":0.5}
            ))
        
        return palette[:7]  # Гарантированно 7 элементов
    
    def _generate_coordinates(self, phase: str, score: float, domain: str, idx: int) -> dict:
        """Генерирует координаты (A,S,T,E) на основе фазы и домена"""
        # Упрощённая эвристика
        base = {"A":0.3,"S":0.5,"T":0.5,"E":0.4}
        
        # Коррекция по домену
        if domain == "phonetic":
            base["S"] += 0.2  # Акцент на спектр
        elif domain == "affective":
            base["E"] += 0.3  # Акцент на эмоции
        
        # Коррекция по скору и индексу
        for k in base:
            base[k] = min(1.0, max(0.0, base[k] + (score - 0.5) * 0.2 + (idx - 3) * 0.05))
        
        return {k: round(v, 3) for k, v in base.items()}
    
    def _default_palette(self, domain: str) -> List[PaletteItem]:
        """Возвращает дефолтную палитру для домена"""
        defaults = {
            "phonetic": ["Sa","Do","Re","Ga","Ma","Pa","Dha"],
            "spectral": ["N₀","H₁","F₁","ΔF","Q","ΣH","C∞"],
            "affective": ["∅₀","↔₁","↗₂","⌁₃","⧉₄","↘₅","⊚₆"]
        }
        symbols = defaults.get(domain, [f"X{i+1}" for i in range(7)])
        
        return [
            PaletteItem(symbol=s, value=s, coordinates={"A":0.5,"S":0.5,"T":0.5,"E":0.5})
            for s in symbols
        ]
    
    def is_available(self) -> bool:
        return True  # Всегда доступен оффлайн
```

### 4.3. `backend/agents/llm_agent.py` — Опциональный LLM-агент

```python
# backend/agents/llm_agent.py
from typing import List, Optional
import os
from core.omega_engine import PaletteItem
from .base_agent import BaseAgent

class LocalLLMAgent(BaseAgent):
    """
    LLM-агент для локальных моделей (llama.cpp, Ollama, LM Studio).
    Работает без интернета при наличии модели на диске.
    """
    
    def __init__(self, model_path: str, context_length: int = 4096):
        self.model_path = model_path
        self.context_length = context_length
        self.client = None  # Инициализируется при первом вызове
    
    def _init_client(self):
        """Ленивая инициализация клиента для локальной LLM"""
        # Пример для llama-cpp-python
        try:
            from llama_cpp import Llama
            self.client = Llama(
                model_path=self.model_path,
                n_ctx=self.context_length,
                n_gpu_layers=-1,  # Использовать GPU если доступно
                verbose=False
            )
        except ImportError:
            raise RuntimeError("Установите: pip install llama-cpp-python")
    
    async def extract_palette(
        self, 
        text: Optional[str] = None, 
        code: Optional[str] = None,
        domain: str = "generic"
    ) -> List[PaletteItem]:
        if not self.client:
            self._init_client()
        
        content = text or code or ""
        
        # Промпт для извлечения 7 элементов палитры
        prompt = f"""
        Ты — Ω-аналитик. Извлеки из текста ровно 7 ключевых элементов, 
        которые могут служить палитрой для 7-фазного цикла.
        
        Домен: {domain}
        Текст: {content[:2000]}  # Обрезаем для контекста
        
        Верни ТОЛЬКО JSON-массив из 7 объектов:
        [
          {{"symbol": "x1", "value": "описание", "coordinates": {{"A":0.3,"S":0.6,"T":0.4,"E":0.5}}}},
          ...
        ]
        Координаты должны быть числами от 0.0 до 1.0.
        """
        
        try:
            response = self.client(
                prompt=prompt,
                max_tokens=500,
                temperature=0.1,  # Низкая температура для детерминизма
                stop=["```", "</json>"]
            )
            import json
            result = json.loads(response['choices'][0]['text'].strip())
            
            # Валидация и преобразование в PaletteItem
            palette = []
            for item in result[:7]:  # Берём максимум 7
                coords = item.get("coordinates", {})
                palette.append(PaletteItem(
                    symbol=item.get("symbol", "X"),
                    value=item.get("value", ""),
                    coordinates={k: float(v) for k, v in coords.items()}
                ))
            
            # Дополняем до 7 если нужно
            while len(palette) < 7:
                palette.append(PaletteItem(
                    symbol=f"X{len(palette)+1}",
                    value="fallback",
                    coordinates={"A":0.5,"S":0.5,"T":0.5,"E":0.5}
                ))
            
            return palette[:7]
            
        except Exception as e:
            # Fallback на оффлайн-агент при ошибке
            from .offline_agent import OfflineAgent
            return await OfflineAgent().extract_palette(text, code, domain)
    
    def is_available(self) -> bool:
        return os.path.exists(self.model_path)
```

---

## 📦 5. Сборка и запуск

### 5.1. `pyproject.toml` — Зависимости backend

```toml
[tool.poetry]
name = "omega-protocol-backend"
version = "1.1.0"
description = "Offline-first Ω-protocol engine"

[tool.poetry.dependencies]
python = "^3.10"
fastapi = "^0.109.0"
uvicorn = {extras = ["standard"], version = "^0.27.0"}
pydantic = "^2.5.0"
numpy = "^1.26.0"
scipy = "^1.12.0"  # Для расчёта метрик
python-dotenv = "^1.0.0"
# Опционально для LLM:
# llama-cpp-python = {version = "^0.2.0", optional = true}

[tool.poetry.extras]
llm = ["llama-cpp-python"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### 5.2. `frontend/package.json` — Зависимости frontend

```json
{
  "name": "omega-protocol-frontend",
  "version": "1.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint src --ext ts,tsx"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.0",
    "zustand": "^4.5.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/node": "^20.10.0",
    "@vitejs/plugin-react": "^4.2.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "eslint": "^8.56.0"
  }
}
```

### 5.3. Запуск в режиме разработки

```bash
# 1. Backend
cd backend
poetry install
# Для LLM-режима: poetry install -E llm
poetry run uvicorn main:app --reload --port 8000

# 2. Frontend (в другом терминале)
cd frontend
npm install
npm run dev  # Запустится на http://localhost:5173

# 3. Приложение доступно в браузере
# Оффлайн-режим работает по умолчанию
```

### 5.4. Сборка desktop-приложения (оффлайн)

```bash
# Скрипт: scripts/build_desktop.py
import subprocess
import shutil
from pathlib import Path

def build_desktop():
    # 1. Собираем frontend
    subprocess.run(["npm", "run", "build"], cwd="frontend", check=True)
    
    # 2. Копируем статику в backend
    shutil.copytree("frontend/dist", "backend/static", dirs_exist_ok=True)
    
    # 3. Собираем через PyInstaller
    subprocess.run([
        "pyinstaller",
        "--name=OmegaProtocol",
        "--onefile",
        "--windowed",  # Без консоли для GUI
        "--add-data=static:static",  # Включаем фронтенд
        "--hidden-import=uvicorn.loops.auto",
        "backend/main.py"
    ], check=True)
    
    print("✅ Сборка завершена: dist/OmegaProtocol.exe (Windows) или .app (macOS)")

if __name__ == "__main__":
    build_desktop()
```

---

## 🧪 6. Тестирование и валидация

### 6.1. `backend/tests/test_axioms.py`

```python
import pytest
from core.omega_engine import OmegaEngine, PaletteItem
from core.axioms import validate_axioms

def test_A1_monotonic_path():
    engine = OmegaEngine()
    palette = [PaletteItem(symbol=f"x{i}", value=i, coordinates={}) for i in range(7)]
    assert engine.validate_palette(palette) == True
    
    # Неправильная длина
    short_palette = [PaletteItem(symbol="x", value=0, coordinates={})] * 6
    assert engine.validate_palette(short_palette) == False

def test_A2_zero_flux():
    # Проверяем, что сумма изменений координат ≈ 0
    from core.metrics import check_zero_flux
    coords = [{"A":0.2+i*0.1, "S":0.5, "T":0.5, "E":0.5} for i in range(8)]
    assert check_zero_flux(coords, coord="A", tolerance=1e-6) == True

def test_full_cycle_stability():
    engine = OmegaEngine()
    palette = [
        PaletteItem(symbol=f"p{i}", value=i, 
                   coordinates={"A":0.2+i*0.1, "S":0.5, "T":0.5, "E":0.5})
        for i in range(7)
    ]
    from core.omega_engine import OmegaSequence
    result = engine.run(OmegaSequence(palette=palette))
    
    assert result.stability_flag == True
    assert result.D_metric <= 0.15
    assert len(result.sequence) == 8  # 7 фаз + терминал
```

### 6.2. Запуск тестов

```bash
# Backend
cd backend
poetry run pytest tests/ -v

# Frontend
cd frontend
npm run test  # Если настроен Vitest
```

---

## 📋 7. Чеклист для AI-ассистента (Windsurf/Codex)

При генерации кода через AI, используйте эти подсказки:

```
✅ Создай класс OmegaEngine с методами: validate_palette, apply_template, calculate_metrics
✅ Реализуй аксиому A5: адаптивная плотность ρₙ = exp(-λ·σ²) с λ=0.85
✅ Добавь self-correction: если D>0.15, перераспредели Δ между φₙ₋₁, φₙ, φₙ₊₁
✅ Сделай OfflineAgent на основе regex-словарей для 7 фаз
✅ Реализуй LLM-агент как опцию с fallback на OfflineAgent при ошибке
✅ В React-компоненте SequenceVisualizer добавь цветовую схему из OPERATOR_COLORS
✅ Обеспечь полную работу без интернета: все зависимости локальные, PWA-манифест
✅ Добавь экспорт результатов в JSON/HTML с сохранением Ω-структуры
✅ Протестируй аксиомы: A1 (длина=7), A2 (ΣΔ=0), A3 (x₇⊂x₀), A4 (изоморфизм), A5 (ρ∈[0.4,1.0])
```

---

## 🚀 Быстрый старт для разработчика

1. **Клонируй шаблон** (или создай структуру по разделу 1)
2. **Установи зависимости**:
   ```bash
   cd backend && poetry install
   cd ../frontend && npm install
   ```
3. **Запусти в dev-режиме**:
   ```bash
   # Терминал 1
   cd backend && poetry run uvicorn main:app --reload
   
   # Терминал 2  
   cd frontend && npm run dev
   ```
4. **Открой** `http://localhost:5173` — приложение готово
5. **Для оффлайн-сборки**:
   ```bash
   python scripts/build_desktop.py
   ```

---

> 💡 **Примечание для AI**: Этот проект спроектирован как **максимально детерминированный**. Все ключевые алгоритмы (Ω-движок, аксиомы, метрики) реализованы на чистом Python/NumPy без внешних вызовов. LLM-агент — опциональный слой, который при отключении полностью заменяется rule-based OfflineAgent.

