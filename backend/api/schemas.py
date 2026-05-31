from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from backend.core.models import OmegaResult, OperatorDefinition


class AnalyzeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=1)
    domain: str = "generic"


class AnalyzeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    result: OmegaResult


class OperatorsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    operators: list[OperatorDefinition]


class ExportRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=1)
    domain: str = "generic"
