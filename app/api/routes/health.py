"""
Health Check Route.

A health endpoint is standard in every production API.
It tells load balancers, monitoring tools, and developers
that the service is running correctly.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["System"])
async def health_check():
    """
    Returns the health status of the API.

    TODO:
    Return a dictionary with:
    - status: "healthy"
    - app: the app name from settings
    - version: the app version from settings

    Hint: import settings from app.config
    """
    pass