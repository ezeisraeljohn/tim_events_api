from sqlalchemy import Column, String, Integer, DateTime
from ..database import Base
from datetime import datetime, timezone

class BaseModel():
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        created_at = Column(DateTime, default=datetime.now(timezone.utc))
        updated_at = Column(DateTime, onupdate=datetime.now(timezone.utc))
