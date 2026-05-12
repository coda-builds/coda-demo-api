from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import agent, rag, search, security

app = FastAPI(
    title="Coda Builds Demo API",
    description="One backend powering Coda Builds live AI demos.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://codabuilds.co.uk",
        "https://www.codabuilds.co.uk",
        "https://coda-builds.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent.router)
app.include_router(rag.router)
app.include_router(search.router)
app.include_router(security.router)


@app.get("/")
def root():
    return {"status": "ok", "service": "Coda Builds Demo API"}


@app.get("/health")
def health():
    return {"status": "healthy"}
