import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Probability of zero events
    prob = math.exp(-lam)

    # Initialize CDF
    cdf = prob

    # Calculate probabilities from 1 to k
    for i in range(1, k + 1):

        # Calculate next probability
        prob = prob * lam / i

        # Add probability to CDF
        cdf += prob
        
    return {
        "pmf": float(prob),
        "cdf": float(cdf)
    }