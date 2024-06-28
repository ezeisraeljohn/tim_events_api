from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from ..database import Base
from .models_base import BaseModel

class Event(BaseModel, Base):

        __tablename__ = "events"

        name = Column(String(255))
        description = Column(Text)
        location = Column(String(255))
        start_time = Column(DateTime)
        end_time = Column(DateTime)
        organizer_id = Column(Integer, ForeignKey('users.id'))

        user = relationship("User", back_populates='events')
        speakers = relationship("Speaker", back_populates='event')
