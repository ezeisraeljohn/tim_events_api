from pydantic import BaseModel


class SpeakerBase(BaseModel):
        first_name: str
        last_name: str
        location: str
        bio: str


class SpeakerCreate(SpeakerBase):
        pass

class SpeakerUpdate(SpeakerBase):
        pass

class Speaker(SpeakerBase):
        id: int
        event_id: int

        class Config:
                orm_mode = True


