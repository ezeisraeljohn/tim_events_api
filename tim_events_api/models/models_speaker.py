from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from .models_base import BaseModel


class Speaker(BaseModel, Base):
      __tablename__ = 'speakers'

      first_name = Column(String(60))
      last_name = Column(String(60))
      bio = Column(Text)
      profile_picture = Column(String(255), nullable=True)
      contact_info = Column(String(255))
      event_id = Column(Integer, ForeignKey('events.id'))

      event = relationship("Event", back_populates="speakers")