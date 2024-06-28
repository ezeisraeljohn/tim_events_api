from fastapi import APIRouter, Depends, HTTPException, status
from ..crud.events import *
from ..schemas import schema_events, schema_users
from ..dependencies import get_db
from ..crud.users import get_current_user

router = APIRouter(
        dependencies=[Depends(get_current_user)],
        prefix="/users/me",
        tags=["events"]
        )


@router.post("/events", response_model=schema_events.Event)
def create_event(
        event: schema_events.EventCreate,
        db: Session=Depends(get_db),
        current_user: schema_users.User = Depends(get_current_user)
        ):
        events = add_event(db=db, event=event, user_id=current_user.id)
        return events


@router.get("/events", response_model=list[schema_events.Event])
def read_events(
        skip: int=0,
        limit: int=100,
        db: Session=Depends(get_db),
        current_user: schema_users.User = Depends(get_current_user)
        ):
        events = get_events(user_id=current_user.id, 
                            skip=skip,
                            limit=limit, db=db
                            )
        return events

@router.get("/events/{event_id}/", response_model=schema_events.Event)
def read_event(
               event_id: int,
               db: Session=Depends(get_db)
               ):
        event = get_event(event_id=event_id, db=db)
        if not event:
                raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="event does not exist"
                        )
        return event

@router.put("/events/{event_id}/", response_model=schema_events.Event)
def update_event(
        event_id: int,
        event: schema_events.EventUpdate,
        current_user: schema_users = Depends(get_current_user),
        db: Session=Depends(get_db)
        ):

        db_event = get_event(event_id=event_id, db=db)
        if not db_event:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="event does not exist"
                                    )
        event_ids = []
        for user_events in current_user.events:
                event_ids.append(user_events.id)

        if event_id not in event_ids:
                raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail= "You cannot update this user"
                )
        
        updated_event = edit_event(event=event, event_id=event_id, db=db)
        return updated_event

@router.delete("/events/{event_id}/")
def delete_event(event_id: int, db: Session=Depends(get_db)):
        return remove_event(event_id=event_id, db=db)
