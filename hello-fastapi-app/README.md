# Hello FastAPI App

A minimal FastAPI application exposing two HTTP endpoints:

- `GET /` → returns JSON: `{ "message": "Hello, World!" }`
- `GET /health` → returns JSON health status: `{ "status": "ok" }`

## Prerequisites

- **Python**: 3.10+ (tested with 3.11)
- **pip**: latest recommended
- **(Optional) Docker**: 20.10+ if you prefer running via container

## Run Locally (without Docker)

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate

Test: trigger CI on test-ci-fix branch