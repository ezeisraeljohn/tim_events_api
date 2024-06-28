from pydantic import BaseModel

class VenueBase(BaseModel):
        name: str
        location: str
        capacity: str
        description: str

class VenueCreate(VenueBase):
        pass

class VenueUpdate(VenueBase):
        pass

class Venue(VenueBase):
        id: int

        class Config:
                from_attributes = True

