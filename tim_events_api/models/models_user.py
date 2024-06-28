from sqlalchemy import Column, String, Integer, DateTime, Boolean
from ..database import Base
from .models_base import BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
        __tablename__ = 'users'

        first_name = Column(String(60))
        username = Column(String(70))
        last_name = Column(String(60))
        email = Column(String(60))
        hashed_password = Column(String(60))
        is_active = Column(Boolean, default=True)
        is_organizer = Column(Boolean, default=True)
        is_admin = Column(Boolean, default=False)

        events = relationship("Event", back_populates="user")
       

        def __str__(self):
                return(f"{self.first_name} {self.last_name}")
        
