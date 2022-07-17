from sqlalchemy.orm import Session
from app.core.types import Coordinates, Point
from app.models.tracks import Tracks

def get_track(db: Session, track_id: int) -> Tracks:
    return db.query(Tracks).filter_by(track_id=track_id).one()

def create_track(db: Session, coords: Coordinates, start_points: Point) -> Tracks:
    new_track = Tracks(coordinates=coords, start_points=start_points)
    db.add(new_track)
    db.flush()
    db.commit()
    
    return new_track