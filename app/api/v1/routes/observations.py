from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List


from app.db.models.observation import Observation
from app.schemas.observation import ObservationRead
from app.db.session import get_db
from app.db.crud import observation as observation_crud




router = APIRouter()

@router.post("/", response_model=ObservationRead)
def create_observation(
    site_visit_id: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    recommendation: Optional[str] = Form(None),
    action_type: Optional[str] = Form(None),
    hazard: Optional[str] = Form(None),
    template_id: Optional[str] = Form(None),
    original_observation_id: Optional[str] = Form(None),
    photo: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    photo_path = None

    if photo:
        file_location = f"uploads/{photo.filename}"
        with open(file_location, "wb") as buffer:
            buffer.write(photo.file.read())
        photo_path = file_location
    
    # Convert empty string to None and ensure integer type if applicable
    template_id = int(template_id) if template_id and template_id.isdigit() else None
    original_observation_id = int(original_observation_id) if original_observation_id and original_observation_id.isdigit() else None


    obs_data = Observation(
        site_visit_id=site_visit_id,
        title=title,
        description=description,
        recommendation=recommendation,
        action_type=action_type,
        hazard=hazard,
        template_id=template_id,
        original_observation_id=original_observation_id,
        photo_path=photo_path,
    )
    db.add(obs_data)
    db.commit()
    db.refresh(obs_data)
    return obs_data


@router.get("/{observation_id}", response_model=ObservationRead)
def get_observation(observation_id: int, db: Session = Depends(get_db)):
    return observation_crud.get_observation(db, observation_id)

@router.get("/", response_model=List[ObservationRead])
def get_all_observations(db: Session = Depends(get_db)):
    return observation_crud.get_all_observations(db)
