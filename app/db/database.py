"""
Database connection and session management.

SQLAlchemy is used as the ORM (Object Relational Mapper).
This file sets up:
  - The database engine (the connection to PostgreSQL)
  - The session factory (creates individual database sessions)
  - A base class for all database models
  - A dependency function for FastAPI route injection
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from app.config import settings

# TODO 1:
# Create the SQLAlchemy engine using settings.database_url
# Hint: use create_engine()
engine = None  # Replace this line


# TODO 2:
# Create a SessionLocal class using sessionmaker
# Set autocommit=False and autoflush=False
# Hint: SessionLocal = sessionmaker(...)
SessionLocal = None  # Replace this line


# Base class that all models will inherit from
# Do not modify this line
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a database session.

    This function:
    1. Creates a new database session
    2. Yields it to the route function
    3. Closes it automatically when the request is done

    Usage in a route:
        @router.get("/example")
        def example(db: Session = Depends(get_db)):
            ...

    TODO 3:
    Implement this function using a try/finally block.
    - Create a db session from SessionLocal
    - yield the session
    - always close the session in the finally block
    """
    pass