from sqlalchemy.orm import Session
from app.db.models.observation_template import ObservationTemplate
from app.schemas.observation_template import ObservationTemplateCreate

def create_template(db: Session, template: ObservationTemplateCreate):
    db_obj = ObservationTemplate(**template.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_template(db: Session, template_id: int):
    return db.query(ObservationTemplate).filter(ObservationTemplate.id == template_id).first()

def get_all_templates(db: Session):
    return db.query(ObservationTemplate).all()
