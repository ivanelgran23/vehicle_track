from math import degrees
from typing import List, Union
from itertools import compress

from geopy import distance
from trianglesolver import solve

from app.core.types import Coordinates


def cos_law(coords: Coordinates, deg_tresh: float = 30.0) -> Coordinates:
    """Calculates the angle between the three coordinates according to the law of cosines

    Args:
        coords (Coordinates): Coordinates
        degTresh (float, optional): Threshold value of the minimum angle between points. Defaults to 30.0.

    Returns:
        Coordinates: Set of coordinates without peak points
    """
    is_spike = [True]
    deg_tresh = float(deg_tresh)
    for i in range(len(coords) - 2):
        d1 = distance.distance(coords[0 + i], coords[1 + i])
        d2 = distance.distance(coords[1 + i], coords[2 + i])
        d3 = distance.distance(coords[2 + i], coords[0 + i])
        d1 = float(str(d1)[:-3]) * 1000
        d2 = float(str(d2)[:-3]) * 1000
        d3 = float(str(d3)[:-3]) * 1000

        if d1 > 0.01 and d2 > 0.01 and d3 > 0.01:
            _, _, _, A, B, C = solve(
                a=d1, b=d2, c=d3
            )  # Calculate the angles from the sides
            A, B, C = degrees(A), degrees(B), degrees(C)  # Convert to math.degrees
            if (360.0 - deg_tresh) < C or C < deg_tresh:
                is_spike.append(False)
            else:
                is_spike.append(True)
        else:
            is_spike.append(True)

    return list(compress(coords, is_spike))
