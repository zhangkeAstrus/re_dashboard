from pydantic import BaseModel
from typing import Optional

class ObservationBase(BaseModel):
    title: str
    description: str
    recommendation: Optional[str] = None
    action_type: Optional[str] = None
    hazard: Optional[str] = None
    template_id: Optional[int] = None
    original_observation_id: Optional[int] = None

class ObservationCreate(ObservationBase):
    site_visit_id: int
    photo_path: Optional[str] = None  # File path or URL

class ObservationRead(ObservationBase):
    id: int
    site_visit_id: int
    photo_path: Optional[str] = None

    class Config:
        orm_mode = True
