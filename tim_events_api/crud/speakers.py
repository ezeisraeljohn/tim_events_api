
"""This module contains functions that interact with the database to perform CRUD operations on the speakers table.
The functions are:
- get_speaker: Get a single speaker by its id.
- get_speakers: Get all speakers for a user.
- add_speaker: Add a speaker to the database.
- edit_speaker: Edit a speaker in the database.
- remove_speaker: Remove a speaker from the database.

each function interacts with the database session object to perform the CRUD operations.
For more information on how to perform CRUD operations,
see: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-crud-utilities
"""

from sqlalchemy.orm import Session
from ..models import models_speaker, models_user
from ..schemas import schema_speakers


def get_speaker(db: Session, speaker_id: int):
        """Get a single speaker by its id.
        Args:
        db (Session): The database session.
        speaker_id (int): The id of the speaker.

        Returns:
        Speaker: The speaker object.
        """
        return db.query(models_speaker.Speaker).filter(models_speaker.Speaker.id == speaker_id).first()


def get_speakers(user_id: int, db: Session, skip: int = 0, limit: int = 100):
        """Get all speakers for a user.
        Args:
        user_id (int): The id of the user.
        db (Session): The database session.
        skip (int): The number of speakers to skip.
        limit (int): The number of speakers to return.

        Returns:
        List[Speaker]: A list of speaker objects.
        """
        return db.query(models_speaker.Speaker).filter(models_user.User.id == user_id).offset(skip).limit(limit).all()



def add_speaker(db: Session, speaker: schema_speakers.SpeakerCreate):
        """Add a speaker to the database.
        Args:
        db (Session): The database session.
        speaker (SpeakerCreate): The speaker data.
        event_id (int): The id of the event.

        Returns:
        Speaker: The speaker object.
        """
        db_speaker = models_speaker.Speaker(**speaker.dict())
        db.add(db_speaker)
        db.commit()
        db.refresh(db_speaker)
        return db_speaker

def edit_speaker(db:Session, speaker_id: int, speaker:schema_speakers.SpeakerUpdate):
        """Edit a speaker in the database.
        Args:
        db (Session): The database session.
        speaker_id (int): The id of the speaker.
        speaker (SpeakerUpdate): The speaker data.

        Returns:
        Speaker: The speaker object.
        """
        db_speaker = db.query(models_speaker.Speaker).filter(models_speaker.Speaker.id == speaker_id).first()
        speaker_dict = speaker.dict()

        for key, value in speaker_dict.items():
                setattr(db_speaker, key, value)
        db.commit()
        db.refresh(db_speaker)
        return db_speaker

def remove_speaker(db: Session, speaker_id: int):
        """Remove a speaker from the database.
        Args:
        db (Session): The database session.
        speaker_id (int): The id of the speaker.

        Returns:
        Dict: An empty dictionary.
        """
        db_speaker = db.query(models_speaker.Speaker).filter(models_speaker.Speaker.id == speaker_id).first()
        db.delete(db_speaker)
        db.commit()
        return {}