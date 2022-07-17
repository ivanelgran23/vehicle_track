import numpy as np

from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from kneed import KneeLocator

from app.core.types import Coordinates


def epsilon_selection(coords: Coordinates) -> float:
    """Selecting the optimal epsilon value for DBSCAN using the 'knee' search method

    Args:
        coords (Coordinates): Coordinates

    Returns:
        float: Epsilon value
    """
    nearest_neighbors = NearestNeighbors(n_neighbors=11)
    neighbors = nearest_neighbors.fit(coords)

    distances, _ = neighbors.kneighbors(coords)
    distances = np.sort(distances[:, 10], axis=0)
    i = np.arange(len(distances))
    knee = KneeLocator(
        i,
        distances,
        S=1,
        curve="convex",
        direction="increasing",
        interp_method="polynomial",
    )

    return distances[knee.knee]


def dbscan(coords: Coordinates, min_points: int) -> Coordinates:
    """Sifting out unnecessary points by DBSCAN clustering method. The output should be only one, the largest cluster

    Args:
        coords (Coordinates): Coordinates
        min_points (int): Minimum number of points to form a cluster

    Returns:
        Coordinates: A set of coordinates representing one large cluster
    """
    min_points = int(min_points)
    clustering = DBSCAN(
        eps=epsilon_selection(coords) / 6371,
        min_samples=min_points,
        algorithm="ball_tree",
        metric="haversine",
    ).fit(np.radians(coords))
    labels = np.reshape(clustering.labels_, (len(clustering.labels_), 1))
    new_coords = np.concatenate((coords, labels), axis=1)

    return new_coords[new_coords[:, 2] == -1][:,:2].tolist()
