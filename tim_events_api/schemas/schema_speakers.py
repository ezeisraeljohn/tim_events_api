from pydantic import BaseModel


class SpeakerBase(BaseModel):
    first_name: str
    last_name: str
    contact_info: str
    bio: str
    event_id: int


class SpeakerCreate(SpeakerBase):
    pass


class SpeakerUpdate(SpeakerBase):
    pass


class Speaker(SpeakerBase):
    id: int

    class Config:
        orm_mode = True
