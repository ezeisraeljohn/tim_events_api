from sqlalchemy.orm import Session
from ..models import models_venue
from ..schemas import schema_venues


def get_venue(db: Session, venue_id: int):
        return db.query(models_venue.Venue).filter(models_venue.Venue.id == venue_id).first()


def get_venues(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models_venue.Venue).offset(skip).limit(limit).all()


def add_venue(db: Session, venue: schema_venues.VenueCreate):
        db_venue = models_venue.Venue(**venue.dict())
        db.add(db_venue)
        db.commit()
        db.refresh(db_venue)
        return db_venue

def edit_venue(db:Session, venue_id: int, venue:schema_venues.VenueUpdate):
        db_venue = db.query(models_venue.Venue).filter(models_venue.Venue.id == venue_id).first()
        venue_dict = venue.dict()

        for key, value in venue_dict.items():
                setattr(db_venue, key, value)
        db.commit()
        db.refresh(db_venue)
        return db_venue

def remove_venue(db: Session, venue_id: int):
        db_venue = db.query(models_venue.venue).filter(models_venue.venue.id == venue_id).first()
        db.delete(db_venue)
        db.commit()
        return {}