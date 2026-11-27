# Correlation lies b/w: -1 to +1 =>
#  +1 = both features are increasing
#  -1 = one Feature is increasing and other is decreasing at the same time.
#  0 = No linear relationship is there.

import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Correlation = Covariance/ (Standard deviation of 1st Feature  X Stand. Dev. of 2nd Feature)

    # Step1: Input List -> Numpy array
    X = np.asarray(X, dtype= float)
    # Step2: Calculate Covariance matrix (Σ) : How both coulmns are changing?
    cov = np.cov(X, rowvar=False)
    # Standard Deviation: How each column is spread?
    std = np.sqrt(np.diag(cov))
    denominator = np.outer(std, std)
    # Step3: Calculating Variance from Covariance Matrix (Diagonals) -> then SD
    # Step4: Pair wise product of Standard Deviatons
    with np.errstate(divide='ignore', invalid='ignore'):  
# division related warnings should be ignored and Invalid Mathematical operations warnings must be ignored
        corr = cov / denominator

    # The place wherever 0 is there make it nan
    corr[denominator == 0] = np.nan  

    return corr