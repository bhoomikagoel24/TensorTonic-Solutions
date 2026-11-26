import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """

    X = np.array(X)
   # Number of samples
    n = X.shape[0]

    # Mean of each feature/column
    mu = np.mean(X, axis=0)

    # Center each feature
    Xc = X - mu

    # Sample covariance matrix
    covariance = (Xc.T @ Xc) / (n - 1)

    return covariance