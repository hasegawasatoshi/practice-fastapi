from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, dependencies, schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db)
) -> Any:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
