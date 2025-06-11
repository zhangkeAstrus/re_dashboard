from pydantic import BaseModel
from typing import Optional

class ObservationTemplateBase(BaseModel):
    title: str
    description: str
    severity: Optional[str] = None
    recommendation: Optional[str] = None

class ObservationTemplateCreate(ObservationTemplateBase):
    pass

class ObservationTemplateRead(ObservationTemplateBase):
    id: int

    class Config:
        orm_mode = True
