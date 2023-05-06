from typing import Any
from fastapi import Depends
from fastapi import APIRouter
from app import crud, schemas, dependencies
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=list[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db)
) -> Any:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
