# omega-invariants

Offline-first extractor and validator for 7-phase Omega structural invariants in text, code, and process descriptions.

## Current Stage

This repository is in the bootstrap phase.

Implemented at this stage:
- canonical specification in [SPEC.md](/D:/WORK/invariants_extractor/SPEC.md)
- project task list in [TASKLIST.md](/D:/WORK/invariants_extractor/TASKLIST.md)
- repository scaffold for backend/frontend development

Deferred for later stages:
- local LLM support
- desktop packaging
- PWA mode
- deep recursion modes

## Local Development

Requirements:
- Python 3.10+
- Poetry
- Node.js 18+
- npm

Backend:

```bash
cd backend
poetry install
poetry run uvicorn main:app --reload --port 8000
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Frontend default URL:
- `http://localhost:5173`

## Repository Layout

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

## Next Build Step

The next implementation stage is:
1. backend domain models
2. `OmegaEngine` skeleton
3. `OfflineAgent` MVP
4. `POST /analyze`
