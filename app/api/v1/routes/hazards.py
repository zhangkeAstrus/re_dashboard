from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.hazard import HazardCreate, HazardRead
from app.db.crud import hazard as hazard_crud
from typing import List

router = APIRouter()

@router.get("/", response_model=list[HazardRead])
def read_hazards(db: Session = Depends(get_db)):
    return hazard_crud.get_all_hazards(db)


@router.post("/", response_model=HazardRead)
def create_hazard(hazard: HazardCreate, db: Session = Depends(get_db)):
    return hazard_crud.create_hazard(db, hazard)
