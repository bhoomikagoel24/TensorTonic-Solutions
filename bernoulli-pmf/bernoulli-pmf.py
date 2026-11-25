import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x = np.array(x)
    
    # If x = 0 → 1-p, if x = 1 → p
    pmf = np.where(x == 0, 1 - p, p)
    mean = p
    variance = p*(1-p)
    
    return {
        "pmf": pmf,
        "mean": float(mean),
        "variance": float(variance)
    }