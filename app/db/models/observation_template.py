from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class ObservationTemplate(Base):
    __tablename__ = "observation_templates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String)
    recommendation = Column(Text)

    # observations = relationship("Observation", back_populates="template")
