from typing import List, Dict
from sqlalchemy.orm import Session
from app.core.types import Coordinates
import app.core.crud.tracks as crud
import app.core.processing as processor

def filter_points(db: Session, filters: List[Dict], track_id: int) -> Coordinates:
    """Applies a set of filters for coordinates

    Args:
        db (Session): Database session
        filters (List[Dict]): Set of functions and arguments
        track_id (int): Coordinate ID in the database

    Returns:
        Coordinates: Processed coordinates
    """    
    track = crud.get_track(db, track_id)
    coords = track.coordinates
    for filter in filters:
        if filter['value'] == 'on':
            coords_handler = getattr(processor, filter['name'])
            args = get_filter_arguments(filters, filter['name'])
            coords = coords_handler(coords, **args)
    
    return coords

def get_filter_arguments(filters: List[Dict], func_name: str) -> Dict:
    """Retrieves from the dictionary with parameters only those that relate to a particular function

    Args:
        filters (List[Dict]): Set of functions and arguments
        func_name (str): A function that needs arguments

    Returns:
        Dict: Arguments for the function
    """    
    args = [{f['name'].split('__')[1]: f['value']} for f in filters if f['name'].startswith(func_name) and f['name'] != func_name]
    
    return {k: v for d in args for k, v in d.items()}