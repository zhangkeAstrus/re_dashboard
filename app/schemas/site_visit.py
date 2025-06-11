from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class SiteVisitBase(BaseModel):
    site_name: str
    visit_date: date
    engineer_id: int
    notes: Optional[str] = None

class SiteVisitCreate(SiteVisitBase):
    pass

class SiteVisitRead(SiteVisitBase):
    id: int

    class Config:
        orm_mode = True
