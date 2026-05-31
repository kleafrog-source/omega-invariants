import { FormEvent, useEffect, useState } from "react";

import { analyzeText, exportResult, fetchOperators } from "./api";
import type { OmegaResult, OperatorDefinition } from "./types";

const DEFAULT_TEXT = `The system starts with an impulse. Then the state becomes stable and steady. Next it shifts and accelerates. After that it switches mode. Then multiple layers merge together. After the peak the signal relaxes and decays. In the final stage the result converges into focus.`;

const DOMAIN_OPTIONS = [
  "generic",
  "text",
  "code",
  "process",
  "phonetic",
  "affective",
  "spectral"
];

export function App() {
  const [text, setText] = useState(DEFAULT_TEXT);
  const [domain, setDomain] = useState("text");
  const [result, setResult] = useState<OmegaResult | null>(null);
  const [operators, setOperators] = useState<OperatorDefinition[]>([]);
  const [loading, setLoading] = useState(false);
  const [exporting, setExporting] = useState<"json" | "html" | null>(null);
  const [bootLoading, setBootLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function bootstrap() {
      try {
        const [operatorPayload, analyzePayload] = await Promise.all([
          fetchOperators(),
          analyzeText({ text: DEFAULT_TEXT, domain: "text" })
        ]);
        setOperators(operatorPayload.operators);
        setResult(analyzePayload.result);
      } catch (bootError) {
        setError(
          bootError instanceof Error
            ? bootError.message
            : "Unable to connect to the backend."
        );
      } finally {
        setBootLoading(false);
      }
    }

    void bootstrap();
  }, []);

  async function handleAnalyze(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const payload = await analyzeText({ text, domain });
      setResult(payload.result);
    } catch (requestError) {
      setError(
        requestError instanceof Error
          ? requestError.message
          : "Analyze request failed."
      );
    } finally {
      setLoading(false);
    }
  }

  async function handleExport(format: "json" | "html") {
    setExporting(format);
    setError(null);

    try {
      const blob = await exportResult(format, { text, domain });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = `omega-analysis.${format}`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(url);
    } catch (requestError) {
      setError(
        requestError instanceof Error
          ? requestError.message
          : "Export request failed."
      );
    } finally {
      setExporting(null);
    }
  }

  return (
    <main className="app-shell">
      <section className="hero-grid">
        <header className="hero-panel">
          <p className="eyebrow">omega-invariants</p>
          <h1>Offline structural extraction for the 7-phase Omega cycle</h1>
          <p className="lede">
            Submit text, code, or process descriptions and inspect the extracted
            sequence, stability metrics, confidence levels, and axiom checks.
          </p>
        </header>

        <section className="control-panel">
          <form className="analyze-form" onSubmit={handleAnalyze}>
            <div className="field-row">
              <label className="field-label" htmlFor="domain">
                Domain
              </label>
              <select
                id="domain"
                className="select-input"
                value={domain}
                onChange={(event) => setDomain(event.target.value)}
              >
                {DOMAIN_OPTIONS.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </div>

            <div className="field-stack">
              <label className="field-label" htmlFor="source-text">
                Source input
              </label>
              <textarea
                id="source-text"
                className="text-input"
                value={text}
                onChange={(event) => setText(event.target.value)}
                rows={10}
              />
            </div>

            <div className="action-row">
              <button className="primary-button" type="submit" disabled={loading}>
                {loading ? "Analyzing..." : "Run analyze"}
              </button>
              <button
                className="ghost-button"
                type="button"
                onClick={() => setText(DEFAULT_TEXT)}
                disabled={loading}
              >
                Reset sample
              </button>
              <button
                className="ghost-button"
                type="button"
                onClick={() => void handleExport("json")}
                disabled={loading || exporting !== null}
              >
                {exporting === "json" ? "Exporting JSON..." : "Export JSON"}
              </button>
              <button
                className="ghost-button"
                type="button"
                onClick={() => void handleExport("html")}
                disabled={loading || exporting !== null}
              >
                {exporting === "html" ? "Exporting HTML..." : "Export HTML"}
              </button>
            </div>
          </form>

          {error ? <div className="error-banner">{error}</div> : null}
          {bootLoading ? <div className="status-banner">Loading backend metadata...</div> : null}
        </section>

        <section className="results-panel">
          <div className="section-heading">
            <h2>Operator palette</h2>
            <span>{operators.length} registered operators</span>
          </div>
          <div className="operator-strip">
            {operators.map((operator) => (
              <article
                className="operator-chip"
                key={operator.internal_id}
                style={{ borderColor: operator.color }}
              >
                <span
                  className="operator-symbol"
                  style={{ backgroundColor: `${operator.color}20`, color: operator.color }}
                >
                  {operator.display_symbol}
                </span>
                <div>
                  <strong>{operator.label}</strong>
                  <p>{operator.ascii_key}</p>
                </div>
              </article>
            ))}
          </div>

          {result ? (
            <>
              <div className="metrics-grid">
                <article className="metric-card">
                  <span>Status</span>
                  <strong className={result.stability_flag ? "ok" : "warn"}>
                    {result.stability_flag ? "Stable" : "Needs review"}
                  </strong>
                </article>
                <article className="metric-card">
                  <span>D metric</span>
                  <strong>{result.D_metric.toFixed(4)}</strong>
                </article>
                <article className="metric-card">
                  <span>Synthetic phases</span>
                  <strong>
                    {result.phase_matches.filter((item) => item.synthetic).length}
                  </strong>
                </article>
                <article className="metric-card">
                  <span>Corrections</span>
                  <strong>{result.corrections_applied.length}</strong>
                </article>
              </div>

              <div className="section-heading">
                <h2>Phase matches</h2>
                <span>{result.sequence.join(" ")}</span>
              </div>

              <div className="phase-list">
                {result.phase_matches.map((phase, index) => {
                  const paletteItem = result.palette[index];
                  const operator = operators.find(
                    (item) => item.internal_id === phase.operator_id
                  );
                  return (
                    <article className="phase-card" key={`${phase.operator_id}-${index}`}>
                      <div className="phase-header">
                        <div className="phase-title">
                          <span
                            className="phase-symbol"
                            style={{
                              backgroundColor: `${operator?.color ?? "#999"}20`,
                              color: operator?.color ?? "#333"
                            }}
                          >
                            {phase.display_symbol}
                          </span>
                          <div>
                            <strong>{operator?.label ?? phase.operator_id}</strong>
                            <p>{phase.operator_id}</p>
                          </div>
                        </div>
                        <div className="phase-meta">
                          <span>{Math.round(phase.confidence * 100)}%</span>
                          {phase.synthetic ? (
                            <span className="synthetic-flag">synthetic</span>
                          ) : null}
                        </div>
                      </div>
                      <p className="phase-text">{phase.source_text}</p>
                      <div className="coords-grid">
                        {Object.entries(paletteItem.coordinates).map(([key, value]) => (
                          <div className="coord-pill" key={key}>
                            <span>{key}</span>
                            <strong>{value.toFixed(3)}</strong>
                          </div>
                        ))}
                      </div>
                    </article>
                  );
                })}
              </div>

              <div className="report-grid">
                <section className="report-card">
                  <div className="section-heading compact">
                    <h2>Validation</h2>
                  </div>
                  <ul className="report-list">
                    <li>{renderCheck("A1 Monotonic path", result.validation.A1_monotonic_path)}</li>
                    <li>{renderCheck("A2 Zero flux", result.validation.A2_zero_flux)}</li>
                    <li>{renderCheck("A3 Recurrent closure", result.validation.A3_recurrent_closure)}</li>
                    <li>{renderCheck("A4 Operator isomorphism", result.validation.A4_operator_isomorphism)}</li>
                    <li>{renderCheck("A5 Adaptive density", result.validation.A5_adaptive_density)}</li>
                  </ul>
                  {result.validation.messages.length > 0 ? (
                    <div className="message-stack">
                      {result.validation.messages.map((message) => (
                        <p key={message} className="warning-message">
                          {message}
                        </p>
                      ))}
                    </div>
                  ) : (
                    <p className="success-message">All configured checks passed.</p>
                  )}
                </section>

                <section className="report-card">
                  <div className="section-heading compact">
                    <h2>Density and corrections</h2>
                  </div>
                  <div className="rho-list">
                    {result.rho_values.map((rho, index) => (
                      <div className="rho-row" key={`${rho}-${index}`}>
                        <span>rho {index + 1}</span>
                        <strong>{rho.toFixed(4)}</strong>
                      </div>
                    ))}
                  </div>
                  <div className="message-stack">
                    {result.corrections_applied.length > 0 ? (
                      result.corrections_applied.map((message) => (
                        <p key={message} className="info-message">
                          {message}
                        </p>
                      ))
                    ) : (
                      <p className="success-message">No corrective pass was required.</p>
                    )}
                  </div>
                </section>
              </div>
            </>
          ) : (
            <div className="status-banner">No analysis result yet.</div>
          )}
        </section>
      </section>
    </main>
  );
}

function renderCheck(label: string, status: boolean) {
  return (
    <span className={`check-item ${status ? "passed" : "failed"}`}>
      <strong>{status ? "PASS" : "FAIL"}</strong>
      <span>{label}</span>
    </span>
  );
}
