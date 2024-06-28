from fastapi import APIRouter, Depends, HTTPException, status
from ..crud.venues import *
from ..schemas import schema_venues
from ..dependencies import get_db
from ..crud.users import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)], tags=["venues"])


@router.post("/venues/", response_model=schema_venues.Venue)
def create_venue(venue: schema_venues.VenueCreate, db: Session=Depends(get_db)):
        return add_venue(db=db, venue=venue)


@router.get("/venues/", response_model=list[schema_venues.Venue])
def read_venues(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
        venues = get_venues(skip=skip, limit=limit, db=db)
        return venues

@router.get("/venues/{venue_id}/", response_model=schema_venues.Venue)
def read_venue(venue_id: int, db: Session=Depends(get_db)):
        venue = get_venue(venue_id=venue_id, db=db)
        if not venue:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="venue does not exist")
        return venue

@router.put("/venues/{venue_id}/", response_model=schema_venues.Venue)
def update_venue(venue_id: int, venue: schema_venues.VenueUpdate, db: Session=Depends(get_db)):
        db_venue = get_venue(venue_id=venue_id, db=db)
        if not db_venue:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="venue does not exist")
        updated_venue = edit_venue(venue=venue, venue_id=venue_id, db=db)
        return updated_venue

@router.delete("/venues/{venue_id}/")
def delete_venue(venue_id: int, db: Session=Depends(get_db)):
        return remove_venue(venue_id=venue_id, db=db)
