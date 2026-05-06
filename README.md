# Coda Builds Demo API

One FastAPI backend powering the live demos for Coda Builds.

## Endpoints

- `GET /health`
- `POST /api/agent/chat`
- `POST /api/rag/query`
- `POST /api/search`
- `POST /api/security/check`

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Deploy on Railway

Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
