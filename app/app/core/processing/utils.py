import itertools

from app.core.types import Coordinates

def get_unique_points(points: Coordinates) -> Coordinates:
    """Remove repetitive elements from the list of points

    Args:
        points (Coordinates): Coordinates

    Returns:
        Coordinates: Unique Coordinates
    """    
    return list(k for k,_ in itertools.groupby(points))