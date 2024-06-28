from sqlalchemy.orm import Session
from ..models import models_event, models_user
from ..schemas import schema_events


def get_event(db: Session, event_id: int):
        return db.query(models_event.Event).filter(models_event.Event.id == event_id).first()


def get_events(user_id: int, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models_event.Event).filter(models_user.User.id == user_id).offset(skip).limit(limit).all()


def add_event(db: Session, event: schema_events.EventCreate, user_id: int):
        db_event = models_event.Event(**event.dict(), organizer_id=user_id)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

def edit_event(db:Session, event_id: int, event:schema_events.EventUpdate):
        db_event = db.query(models_event.Event).filter(models_event.Event.id == event_id).first()
        event_dict = event.dict()

        for key, value in event_dict.items():
                setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
        return db_event

def remove_event(db: Session, event_id: int):
        db_event = db.query(models_event.Event).filter(models_event.Event.id == event_id).first()
        db.delete(db_event)
        db.commit()
        return {}