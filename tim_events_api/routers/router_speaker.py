from fastapi import APIRouter, Depends, HTTPException, status
from ..crud.speakers import *
from ..schemas import schema_speakers, schema_users
from ..dependencies import get_db
from ..crud.users import get_current_user

router = APIRouter(
    prefix="/users/me", dependencies=[Depends(get_current_user)], tags=["speakers"]
)


@router.post("/speakers/", response_model=schema_speakers.Speaker)
def create_speaker(
    speaker: schema_speakers.SpeakerCreate,
    db: Session = Depends(get_db),
    current_user: schema_users.User = Depends(get_current_user),
):
    return add_speaker(db=db, speaker=speaker)


@router.get("/speakers/", response_model=list[schema_speakers.Speaker])
def read_speakers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schema_users.User = Depends(get_current_user),
):
    speakers = get_speakers(user_id=current_user.id, skip=skip, limit=limit, db=db)
    return speakers


@router.get("/speakers/{speaker_id}/", response_model=schema_speakers.Speaker)
def read_speaker(speaker_id: int, db: Session = Depends(get_db)):
    speaker = get_speaker(speaker_id=speaker_id, db=db)
    if not speaker:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="speaker does not exist"
        )
    return speaker


@router.put("/speakers/{speaker_id}/", response_model=schema_speakers.Speaker)
def update_speaker(
    speaker_id: int,
    speaker: schema_speakers.SpeakerUpdate,
    db: Session = Depends(get_db),
):
    db_speaker = get_speaker(speaker_id=speaker_id, db=db)
    if not db_speaker:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="speaker does not exist"
        )
    updated_speaker = edit_speaker(speaker=speaker, speaker_id=speaker_id, db=db)
    return updated_speaker


@router.delete("/speakers/{speaker_id}/")
def delete_speaker(speaker_id: int, db: Session = Depends(get_db)):
    return remove_speaker(speaker_id=speaker_id, db=db)
