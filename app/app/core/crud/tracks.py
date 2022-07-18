from sqlalchemy.orm import Session
from app.core.types import Coordinates, Point
from app.models.tracks import Tracks

def get_track(db: Session, track_id: int) -> Tracks:
    """Returns the saved track by its ID

    Args:
        db (Session): Database session
        track_id (int): ID of track

    Returns:
        Tracks: DB Track coordinates
    """    
    return db.query(Tracks).filter_by(track_id=track_id).one()

def create_track(db: Session, coords: Coordinates, start_points: Point) -> Tracks:
    """Saves the track with its parameters in the database

    Args:
        db (Session): Database session
        coords (Coordinates): Track coordinates
        start_points (Point): Starting point for map view

    Returns:
        Tracks: DB Track coordinates
    """    
    new_track = Tracks(coordinates=coords, start_points=start_points)
    db.add(new_track)
    db.flush()
    db.commit()
    
    return new_track