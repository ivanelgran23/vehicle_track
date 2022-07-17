from typing import Generator

from app.core.db.engine import Session as SessionLocal


def get_db() -> Generator:
    with SessionLocal.begin() as db:
        yield db
