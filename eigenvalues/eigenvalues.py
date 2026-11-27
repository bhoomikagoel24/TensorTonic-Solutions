import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Convert input into the Numpy Array
    A = np.array(matrix, dtype=float)

    # Calculate eigenvalues and sort them in Ascending order
    e_values = np.linalg.eigvals(A)
    e_values = np.sort(e_values)

    # REturn Numpy array as floats
    return np.asarray(e_values, dtype=float)