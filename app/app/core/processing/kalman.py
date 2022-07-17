import numpy as np

from pykalman import KalmanFilter
from app.core.types import Coordinates


def kalman(coords: Coordinates, n_iter: int = 20) -> Coordinates:
    """Applies the Kalman filter to a set of coordinates, to smooth the entire track

    Args:
        coords (Coordinates): Coordinates
        n_iter (int): Number of iterations

    Returns:
        Coordinates: The set of coordinates that make up the more averaged line
    """
    n_iter = int(n_iter)
    coords = np.asarray(coords)
    
    initial_state_mean = [coords[0, 0], 0, coords[0, 1], 0]

    transition_matrix = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]]

    observation_matrix = [[1, 0, 0, 0], [0, 0, 1, 0]]

    kf1 = KalmanFilter(
        transition_matrices=transition_matrix,
        observation_matrices=observation_matrix,
        initial_state_mean=initial_state_mean,
        em_vars=["transition_covariance", "initial_state_covariance"],
    )

    kf1 = kf1.em(coords, n_iter=n_iter)
    smoothed_state_means, _ = kf1.smooth(coords)

    return np.vstack(
        (smoothed_state_means[:, 0], smoothed_state_means[:, 2])
    ).T.tolist()
