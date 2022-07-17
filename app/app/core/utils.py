import math
import numpy as np

from typing import Tuple, List, Union

from folium import Map, PolyLine
from app.core.types import Coordinates, Point


def build_map_with_track(
    start_points: Tuple[float], coordinates: List[Union[float, float]]
) -> Map:
    """Generating a map using the folium library

    Args:
        start_points (Tuple[float]): The starting position of the map view
        coordinates (List[Union[float, float]]): Track coordinates

    Returns:
        Map: Folium Map object
    """
    folium_map = Map(location=start_points, zoom_start=13)
    PolyLine(coordinates, color="red", weight=5, opacity=0.8).add_to(folium_map)

    return folium_map


def calc_distance(fcoord: Point, scoord: Point) -> float:
    """Calculates the distance between two points

    Args:
        fcoord (Point): First point
        scoord (Point): Second Point

    Returns:
        float: Distance in km
    """    
    lat1 = fcoord[0]
    lat2 = scoord[0]
    lon1 = fcoord[1]
    lon2 = scoord[1]  
    
    # Lon/Lat --> Radians
    dLat = np.deg2rad(lat2 - lat1)
    dLon = np.deg2rad(lon2 - lon1)
    
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(np.deg2rad(lat1)) * math.cos(np.deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6371 * c
    
    return d


def get_distance(points: Coordinates) -> float:
    """Calculates the total distance in kilometers

    Args:
        points (Coordinates): Coordinates

    Returns:
        float: Total distance
    """    
    total_distance = 0
    for i in range(len(points) - 1):
        total_distance += calc_distance(points[0+i], points[1+i])
    
    return round(total_distance, 1)