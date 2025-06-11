from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.crud import site_visit as site_visit_crud
from app.schemas.site_visit import SiteVisitCreate, SiteVisitRead
from typing import List

router = APIRouter()

@router.post("/", response_model=SiteVisitRead)
def create_site_visit(site_visit: SiteVisitCreate, db: Session = Depends(get_db)):
    return site_visit_crud.create_site_visit(db, site_visit)

@router.get("/{site_visit_id}", response_model=SiteVisitRead)
def get_site_visit(site_visit_id: int, db: Session = Depends(get_db)):
    return site_visit_crud.get_site_visit(db, site_visit_id)

@router.get("/", response_model=List[SiteVisitRead])
def get_all_site_visits(db: Session = Depends(get_db)):
    return site_visit_crud.get_all_site_visits(db)
