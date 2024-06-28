from sqlalchemy.orm import Session
from ..models import models_speaker, models_user
from ..schemas import schema_speakers


def get_speaker(db: Session, speaker_id: int):
        return db.query(models_speaker.Speaker).filter(models_speaker.Speaker.id == speaker_id).first()


def get_speakers(user_id: int, db: Session, skip: int = 0, limit: int = 100):
         return db.query(models_speaker.Speaker).filter(models_user.User.id == user_id).offset(skip).limit(limit).all()



def add_speaker(db: Session, speaker: schema_speakers.SpeakerCreate, event_id: int):
        db_speaker = models_speaker.Speaker(**speaker.dict(), event_id=event_id)
        db.add(db_speaker)
        db.commit()
        db.refresh(db_speaker)
        return db_speaker

def edit_speaker(db:Session, speaker_id: int, speaker:schema_speakers.SpeakerUpdate):
        db_speaker = db.query(models_speaker.Speaker).filter(models_speaker.Speaker.id == speaker_id).first()
        speaker_dict = speaker.dict()

        for key, value in speaker_dict.items():
                setattr(db_speaker, key, value)
        db.commit()
        db.refresh(db_speaker)
        return db_speaker

def remove_speaker(db: Session, speaker_id: int):
        db_speaker = db.query(models_speaker.Speaker).filter(models_speaker.Speaker.id == speaker_id).first()
        db.delete(db_speaker)
        db.commit()
        return {}