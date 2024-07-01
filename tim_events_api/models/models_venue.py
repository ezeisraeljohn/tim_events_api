from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from ..database import Base
from .models_base import BaseModel


class Venue(BaseModel, Base):

    __tablename__ = "venues"

    name = Column(String(255))
    location = Column(String(255))
    capacity = Column(Integer)
    description = Column(Text)
