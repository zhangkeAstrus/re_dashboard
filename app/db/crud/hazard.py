from sqlalchemy.orm import Session
from app.db.models.hazard import Hazard
from app.schemas.hazard import HazardCreate


def get_all_hazards(db: Session):
    return db.query(Hazard).all()


def create_hazard(db: Session, hazard: HazardCreate):
    db_hazard = Hazard(name=hazard.name)
    db.add(db_hazard)
    db.commit()
    db.refresh(db_hazard)
    return db_hazard