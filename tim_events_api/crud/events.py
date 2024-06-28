
"""This module defines the CRUD operations for the events table.
The functions are:
- get_event: Get a single event by its id.
- get_events: Get all events for a user.
- add_event: Add an event to the database.
- edit_event: Edit an event in the database.
- remove_event: Remove an event from the database.

each function interacts with the database session object to perform the CRUD operations.
For more information on how to perform CRUD operations,
see: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-crud-utilities

"""
from sqlalchemy.orm import Session
from ..models import models_event, models_user
from ..schemas import schema_events


def get_event(db: Session, event_id: int):
        """Get a single event by its id.
        Args:
        db (Session): The database session.
        event_id (int): The id of the event.
        Returns:
        Event: The event object.
        """
        return db.query(models_event.Event).filter(models_event.Event.id == event_id).first()


def get_events(user_id: int, db: Session, skip: int = 0, limit: int = 100):
        """Get all events for a user.
        Args:
        user_id (int): The id of the user.
        db (Session): The database session.
        skip (int): The number of events to skip.
        limit (int): The number of events to return.
        Returns:
        List[Event]: A list of event objects.
        """
        return db.query(models_event.Event).filter(models_event.Event.organizer_id == user_id).offset(skip).limit(limit).all()


def add_event(db: Session, event: schema_events.EventCreate, user_id: int):
        """Add an event to the database.
        Args:
        db (Session): The database session.
        event (EventCreate): The event data.
        user_id (int): The id of the user.
        Returns:
        Event: The event object.
        """
        db_event = models_event.Event(**event.dict(), organizer_id=user_id)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

def edit_event(db:Session, event_id: int, event:schema_events.EventUpdate):
        """Edit an event in the database.
        Args:
        db (Session): The database session.
        event_id (int): The id of the event.
        event (EventUpdate): The event data.
        Returns:
        Event: The event object.
        """
        db_event = db.query(models_event.Event).filter(models_event.Event.id == event_id).first()
        event_dict = event.dict()

        for key, value in event_dict.items():
                setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
        return db_event

def remove_event(db: Session, event_id: int):
        """Remove an event from the database.
        Args:
        db (Session): The database session.
        event_id (int): The id of the event.
        Returns:
        dict: An empty dictionary.
        """
        db_event = db.query(models_event.Event).filter(models_event.Event.id == event_id).first()
        db.delete(db_event)
        db.commit()
        return {}