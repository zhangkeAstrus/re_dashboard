from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    site_visit_id = Column(Integer, ForeignKey("site_visits.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    # severity = Column(String)
    recommendation = Column(Text)
    hazard = Column(String, nullable=True)
    photo_path = Column(String, nullable = True)
    action_type = Column(String, nullable=True)


    # Optional references to original or template
    # original_observation_id = Column(Integer, ForeignKey("observations.id"), nullable=True)
    # template_id = Column(Integer, ForeignKey("observation_templates.id"), nullable=True)

    site_visit = relationship("SiteVisit", back_populates="observations")
    # original_observation = relationship("Observation", remote_side=[id])
    # template = relationship("ObservationTemplate", back_populates="observations")
