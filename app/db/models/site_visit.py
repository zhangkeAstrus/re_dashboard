from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class SiteVisit(Base):
    __tablename__ = "site_visits"

    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String, nullable=False)
    visit_date = Column(Date, nullable=False)
    engineer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    notes = Column(Text)

    observations = relationship("Observation", back_populates="site_visit")
