from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
from .schema_events import Event


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    is_organizer: bool
    is_admin: bool
    events: list[Event] = []

    class Config:
        orm_mode = True
