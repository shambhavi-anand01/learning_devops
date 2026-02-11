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

## CI: Docker Build & Push (GitHub Actions)

This repository builds and publishes a Docker image to **Docker Hub** when a PR is **merged into `main`**.

### Triggers
- On `push` to `main`: **Build & Push**
- On `push` to test branches (e.g., `test-ci-fix`): **Build only**
- Manual run via **Actions → Run workflow** (optional `semver` tag)

### Tags
- `latest` — only on `main`
- `<short-sha>` — always (first 7 chars of commit SHA)
- `<semver>` — optional (when provided in manual run)

### Secrets required
- `DOCKERHUB_USERNAME` — Docker Hub username
- `DOCKERHUB_TOKEN` — Docker Hub **access token** (Account → Security → New Access Token)

### Build context & Dockerfile
- Context: `./hello-fastapi-app`
- Dockerfile: `./hello-fastapi-app/Dockerfile`
  
