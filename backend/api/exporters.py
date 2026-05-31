from __future__ import annotations

import json
from html import escape

from backend.core.models import OmegaResult, OperatorDefinition


def build_json_export(result: OmegaResult) -> str:
    return json.dumps(result.model_dump(mode="json"), ensure_ascii=False, indent=2)


def build_html_export(
    result: OmegaResult,
    operators: list[OperatorDefinition],
) -> str:
    operator_by_id = {operator.internal_id: operator for operator in operators}

    phase_cards = []
    for phase, palette_item in zip(result.phase_matches, result.palette):
        operator = operator_by_id.get(phase.operator_id)
        color = operator.color if operator else "#666666"
        label = operator.label if operator else phase.operator_id
        synthetic_badge = (
            '<span class="badge synthetic">synthetic</span>' if phase.synthetic else ""
        )
        coords = " ".join(
            f'<span class="coord">{key}: {value:.3f}</span>'
            for key, value in palette_item.coordinates.as_dict().items()
        )
        phase_cards.append(
            f"""
            <article class="phase-card" style="border-color: {color};">
              <div class="phase-head">
                <div class="phase-title">
                  <span class="symbol" style="background:{color}20;color:{color};">{escape(phase.display_symbol)}</span>
                  <div>
                    <strong>{escape(label)}</strong>
                    <p>{escape(phase.operator_id)}</p>
                  </div>
                </div>
                <div class="phase-meta">
                  <span class="badge">{round(phase.confidence * 100)}%</span>
                  {synthetic_badge}
                </div>
              </div>
              <p class="phase-text">{escape(phase.source_text)}</p>
              <div class="coords">{coords}</div>
            </article>
            """
        )

    validation_rows = []
    validation_map = {
        "A1 Monotonic path": result.validation.A1_monotonic_path,
        "A2 Zero flux": result.validation.A2_zero_flux,
        "A3 Recurrent closure": result.validation.A3_recurrent_closure,
        "A4 Operator isomorphism": result.validation.A4_operator_isomorphism,
        "A5 Adaptive density": result.validation.A5_adaptive_density,
    }
    for label, status in validation_map.items():
        validation_rows.append(
            f'<li class="validation {"pass" if status else "fail"}"><strong>{"PASS" if status else "FAIL"}</strong><span>{escape(label)}</span></li>'
        )

    corrections = "".join(
        f'<p class="info">{escape(message)}</p>' for message in result.corrections_applied
    ) or '<p class="success">No corrective pass was required.</p>'

    warnings = "".join(
        f'<p class="warning">{escape(message)}</p>' for message in result.validation.messages
    ) or '<p class="success">All configured checks passed.</p>'

    rho_rows = "".join(
        f'<div class="rho-row"><span>rho {index + 1}</span><strong>{rho:.4f}</strong></div>'
        for index, rho in enumerate(result.rho_values)
    )

    return f"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>omega-invariants export</title>
    <style>
      :root {{
        --bg: #f4f0e8;
        --panel: rgba(255,252,247,0.96);
        --text: #1d1d1b;
        --muted: #5b5f52;
        --border: rgba(29,29,27,0.12);
        --success: #1d7a43;
        --warning: #9f2d2d;
      }}
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        padding: 32px;
        font-family: Georgia, "Times New Roman", serif;
        background:
          radial-gradient(circle at top left, rgba(13, 107, 95, 0.16), transparent 32%),
          radial-gradient(circle at bottom right, rgba(199, 146, 73, 0.18), transparent 28%),
          var(--bg);
        color: var(--text);
      }}
      .shell {{ max-width: 1200px; margin: 0 auto; display: grid; gap: 20px; }}
      .panel {{
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 24px;
      }}
      .metrics {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 12px;
      }}
      .metric, .phase-card, .subpanel {{
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 16px;
        background: rgba(255,255,255,0.68);
      }}
      .phase-list {{ display: grid; gap: 12px; }}
      .phase-head, .phase-title, .phase-meta, .rho-row {{
        display: flex;
        align-items: center;
      }}
      .phase-head {{ justify-content: space-between; gap: 16px; }}
      .phase-title {{ gap: 12px; }}
      .symbol {{
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border-radius: 14px;
        font-weight: 700;
      }}
      .phase-title p, .metric span, .rho-row span {{ margin: 0; color: var(--muted); }}
      .phase-text {{ line-height: 1.7; }}
      .coords {{ display: flex; flex-wrap: wrap; gap: 8px; }}
      .coord, .badge {{
        border-radius: 999px;
        padding: 4px 10px;
        background: rgba(29,29,27,0.08);
      }}
      .synthetic {{ background: rgba(159,45,45,0.12); color: var(--warning); }}
      .report {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 16px;
      }}
      ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; }}
      .validation {{
        display: flex;
        gap: 12px;
        align-items: center;
        border-radius: 14px;
        padding: 10px 12px;
      }}
      .validation.pass {{ background: rgba(29,122,67,0.1); color: var(--success); }}
      .validation.fail {{ background: rgba(159,45,45,0.1); color: var(--warning); }}
      .warning, .success, .info {{
        border-radius: 14px;
        padding: 12px 14px;
      }}
      .warning {{ background: rgba(159,45,45,0.08); color: var(--warning); }}
      .success {{ background: rgba(29,122,67,0.08); color: var(--success); }}
      .info {{ background: rgba(13,107,95,0.08); color: #0d6b5f; }}
      .rho-stack {{ display: grid; gap: 10px; }}
      .rho-row {{
        justify-content: space-between;
        border-radius: 12px;
        padding: 10px 12px;
        background: rgba(244,240,232,0.8);
      }}
    </style>
  </head>
  <body>
    <main class="shell">
      <section class="panel">
        <p>omega-invariants</p>
        <h1>Omega analysis export</h1>
        <p>Sequence: {escape(" ".join(result.sequence))}</p>
      </section>

      <section class="panel metrics">
        <article class="metric"><span>Status</span><strong>{"Stable" if result.stability_flag else "Needs review"}</strong></article>
        <article class="metric"><span>D metric</span><strong>{result.D_metric:.4f}</strong></article>
        <article class="metric"><span>Synthetic phases</span><strong>{sum(1 for item in result.phase_matches if item.synthetic)}</strong></article>
        <article class="metric"><span>Corrections</span><strong>{len(result.corrections_applied)}</strong></article>
      </section>

      <section class="panel">
        <h2>Phase matches</h2>
        <div class="phase-list">
          {"".join(phase_cards)}
        </div>
      </section>

      <section class="panel report">
        <div class="subpanel">
          <h2>Validation</h2>
          <ul>
            {"".join(validation_rows)}
          </ul>
          {warnings}
        </div>
        <div class="subpanel">
          <h2>Density and corrections</h2>
          <div class="rho-stack">{rho_rows}</div>
          {corrections}
        </div>
      </section>
    </main>
  </body>
</html>
    """.strip()
