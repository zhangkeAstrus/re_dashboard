from sqlalchemy.orm import Session
from app.db.models.observation import Observation
from app.schemas.observation import ObservationCreate

def create_observation(db: Session, observation: ObservationCreate):
    db_obj = Observation(**observation.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_observation(db: Session, observation_id: int):
    return db.query(Observation).filter(Observation.id == observation_id).first()

def get_all_observations(db: Session):
    return db.query(Observation).all()
