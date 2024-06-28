import uvicorn
from fastapi import FastAPI
from .routers import router_events, router_speaker, router_users, router_venue
from .database import Base, engine


description = """
### Tim Events API helps you create events for B2B, Networking, Conferences.....

## Users

A User can be a viewer, an organizer or an admin.\
A user will be able to create events, venues and speakers.\
It also supports CRUD operations

## Events

You will be able to:
Perform CRUD Operations on Events

## Speakers.
You will be able to perform CRUD operations on Speakers

## Venues
You will be able to perform CRUD operations on Venues
"""
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "events",
        "description": "Manage events. Manages CRUD operation for events.",
    },
    {
        "name": "speakers",
        "description": "Manage speakers. Manages CRUD operation for speakers.",
    },
    {
        "name": "venues",
        "description": "Manage venues. Manages CRUD operation for venues.",
    },
]

app = FastAPI(
    title="Tim Events API",
    description=description,
    summary="Api for creating events",
    version="0.0.1",
    openapi_tags=tags_metadata
)

Base.metadata.create_all(bind=engine)


app.include_router(router_users.router)
app.include_router(router_events.router)
app.include_router(router_speaker.router)
app.include_router(router_venue.router)

@app.get("/")
def read_root():
    return {"Welcome to the app"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
