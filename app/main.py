"""
DataPulse AI — Main Application Entry Point.

This file:
  1. Creates the FastAPI app instance
  2. Registers all route modules
  3. Sets up startup events
  4. Configures CORS (Cross Origin Resource Sharing)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import health, ingest, query, documents

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered document intelligence API"
)

# CORS — allows the Streamlit frontend to talk to this API
# TODO: In production, replace "*" with your actual frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
# TODO: include all four routers here
# Hint: app.include_router(health.router)
# Do this for health, ingest, query, and documents


@app.on_event("startup")
async def startup_event():
    """
    Runs once when the application starts.
    Good place for initialisation logic.

    TODO:
    Print a startup message showing the app name and version
    from settings. This confirms the app started correctly.
    """
    pass