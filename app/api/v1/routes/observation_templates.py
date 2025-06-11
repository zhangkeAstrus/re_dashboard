from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.crud import observation_template as template_crud
from app.schemas.observation_template import ObservationTemplateCreate, ObservationTemplateRead
from typing import List

router = APIRouter()

@router.post("/", response_model=ObservationTemplateRead)
def create_template(template: ObservationTemplateCreate, db: Session = Depends(get_db)):
    return template_crud.create_template(db, template)

@router.get("/{template_id}", response_model=ObservationTemplateRead)
def get_template(template_id: int, db: Session = Depends(get_db)):
    return template_crud.get_template(db, template_id)

@router.get("/", response_model=List[ObservationTemplateRead])
def get_all_templates(db: Session = Depends(get_db)):
    return template_crud.get_all_templates(db)
