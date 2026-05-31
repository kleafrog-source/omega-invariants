from fastapi import FastAPI
from fastapi.responses import Response

from backend.agents.offline_agent import OfflineAgent
from backend.api.exporters import build_html_export, build_json_export
from backend.api.schemas import AnalyzeRequest, AnalyzeResponse, ExportRequest, OperatorsResponse
from backend.core.omega_engine import OmegaEngine
from backend.core.operators import OPERATORS

app = FastAPI(title="omega-invariants", version="0.1.0")

agent = OfflineAgent()
engine = OmegaEngine()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/operators", response_model=OperatorsResponse)
def operators() -> OperatorsResponse:
    return OperatorsResponse(operators=OPERATORS)


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
    sequence = agent.analyze(content=payload.text, domain=payload.domain)
    result = engine.run(sequence)
    return AnalyzeResponse(result=result)


@app.post("/export/json")
def export_json(payload: ExportRequest) -> Response:
    sequence = agent.analyze(content=payload.text, domain=payload.domain)
    result = engine.run(sequence)
    return Response(
        content=build_json_export(result),
        media_type="application/json",
        headers={
            "Content-Disposition": 'attachment; filename="omega-analysis.json"'
        },
    )


@app.post("/export/html")
def export_html(payload: ExportRequest) -> Response:
    sequence = agent.analyze(content=payload.text, domain=payload.domain)
    result = engine.run(sequence)
    return Response(
        content=build_html_export(result=result, operators=OPERATORS),
        media_type="text/html; charset=utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="omega-analysis.html"'
        },
    )
