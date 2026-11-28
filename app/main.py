from fastapi import FastAPI

from app.config import APP_VERSION

app = FastAPI(
    title="StudyTracker API",
    version=APP_VERSION,
)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    """Verifica que la API esté activa y expone la versión actual."""
    return {
        "status": "ok",
        "database": "pending",
        "version": APP_VERSION,
    }
