from pydantic import BaseModel

class VenueBase(BaseModel):
        name: str
        location: str
        capacity: int
        description: str

class VenueCreate(VenueBase):
        pass

class VenueUpdate(VenueBase):
        pass

class Venue(VenueBase):
        id: int

        class Config:
                orm_mode = True

