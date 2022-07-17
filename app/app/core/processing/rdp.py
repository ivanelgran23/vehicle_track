from math import sqrt

from app.core.types import Coordinates, Point


def distance(a: Point, b: Point) -> float:
    """Calculate distance between points

    Args:
        a (Point): First coordinate
        b (Point): Second coordinate

    Returns:
        float: Distance
    """
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def point_line_distance(point: Point, start: Point, end: Point) -> float:
    if start == end:
        return distance(point, start)
    else:
        n = abs(
            (end[0] - start[0]) * (start[1] - point[1])
            - (start[0] - point[0]) * (end[1] - start[1])
        )
        d = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        return n / d


def rdp(points: Coordinates, epsilon: float) -> Coordinates:
    """Reduces a series of points to a simplified version that loses detail, but
    maintains the general shape of the series.

    Args:
        points (Coordinates): Coordinates
        epsilon (float): Distance dimension

    Returns:
        Coordinates: Similar curve with fewer points
    """
    epsilon = float(epsilon)
    dmax = 0.0
    index = 0
    for i in range(1, len(points) - 1):
        d = point_line_distance(points[i], points[0], points[-1])
        if d > dmax:
            index = i
            dmax = d

    if dmax >= epsilon:
        results = rdp(points[: index + 1], epsilon)[:-1] + rdp(points[index:], epsilon)
    else:
        results = [points[0], points[-1]]

    return results
