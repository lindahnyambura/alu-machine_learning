#!/usr/bin/env python3

"""
Calculates the posterior probability using Bayes' Theorem
"""


from scipy import special


def posterior(x, n, p1, p2):
    """
    Calculates the posterior probability using Bayes' Theorem
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(("x must be an integer that is"
                          " greater than or equal to 0"))
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or not (0 <= p1 <= 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or not (0 <= p2 <= 1):
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Compute the CDF of the Beta distribution at p1 and p2
    alpha = x + 1
    beta = n - x + 1
    cdf_p1 = special.betainc(alpha, beta, p1)
    cdf_p2 = special.betainc(alpha, beta, p2)

    # The posterior probability that p is in the range [p1, p2]
    posterior_prob = cdf_p2 - cdf_p1

    return posterior_prob
