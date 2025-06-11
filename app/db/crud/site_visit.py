from sqlalchemy.orm import Session
from app.db.models.site_visit import SiteVisit
from app.schemas.site_visit import SiteVisitCreate

def create_site_visit(db: Session, site_visit: SiteVisitCreate):
    db_obj = SiteVisit(**site_visit.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_site_visit(db: Session, site_visit_id: int):
    return db.query(SiteVisit).filter(SiteVisit.id == site_visit_id).first()

def get_all_site_visits(db: Session):
    return db.query(SiteVisit).all()
