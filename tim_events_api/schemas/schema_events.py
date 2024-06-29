from pydantic import BaseModel
from .schema_speakers import Speaker
from datetime import datetime

class EventBase(BaseModel):
        name: str
        description: str
        location: str
        start_time:datetime
        end_time: datetime



class EventCreate(EventBase):
        pass

class EventUpdate(EventBase):
        pass

class Event(EventBase):
        id: int
        organizer_id: int
        speakers: list[Speaker] = []
        
        class Config():
                orm_mode = True
