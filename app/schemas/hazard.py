from pydantic import BaseModel

class HazardBase(BaseModel):
    name: str

class HazardCreate(HazardBase):
    pass

class HazardRead(HazardBase):
    id: int

    class Config:
        orm_mode = True