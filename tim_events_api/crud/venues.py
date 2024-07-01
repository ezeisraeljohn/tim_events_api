""" This module contains the CRUD functions for the venues table. 

The functions are:
- get_venue: Get a single venue by its id.
- get_venues: Get all venues.
- add_venue: Add a venue.
- edit_venue: Edit a venue.
- remove_venue: Remove a venue.

Each function interacts with the database session object to perform the CRUD operations.
For more information on how to perform CRUD operations,
see: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-crud-utilities
"""

from sqlalchemy.orm import Session
from ..models import models_venue
from ..schemas import schema_venues


def get_venue(db: Session, venue_id: int):
    """Get a single venue by its id.
    Args:
    db (Session): The database session.
    venue_id (int): The id of the venue.

    Returns:
    Venue: The venue object.
    """
    return (
        db.query(models_venue.Venue).filter(models_venue.Venue.id == venue_id).first()
    )


def get_venues(db: Session, skip: int = 0, limit: int = 100):
    """Get all venues.
    Args:
    db (Session): The database session.
    skip (int): The number of venues to skip.
    limit (int): The number of venues to return.

    Returns:
    List[Venue]: A list of venue objects.
    """
    return db.query(models_venue.Venue).offset(skip).limit(limit).all()


def add_venue(db: Session, venue: schema_venues.VenueCreate):
    """Add a venue.
    Args:
    db (Session): The database session.
    venue (VenueCreate): The venue data.

    Returns:
    Venue: The venue object.
    """
    db_venue = models_venue.Venue(**venue.dict())
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue


def edit_venue(db: Session, venue_id: int, venue: schema_venues.VenueUpdate):
    """Edit a venue.
    Args:
    db (Session): The database session.
    venue_id (int): The id of the venue.
    venue (VenueUpdate): The venue data.

    Returns:
    Venue: The venue object.
    """
    db_venue = (
        db.query(models_venue.Venue).filter(models_venue.Venue.id == venue_id).first()
    )
    venue_dict = venue.dict()

    for key, value in venue_dict.items():
        setattr(db_venue, key, value)
    db.commit()
    db.refresh(db_venue)
    return db_venue


def remove_venue(db: Session, venue_id: int):
    """Remove a venue.
    Args:
    db (Session): The database session.
    venue_id (int): The id of the venue.
    """
    db_venue = (
        db.query(models_venue.venue).filter(models_venue.venue.id == venue_id).first()
    )
    db.delete(db_venue)
    db.commit()
    return {}
