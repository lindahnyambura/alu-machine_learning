#!/usr/bin/env python3

"""
calculates the marginal probability of obtaining
the data given various hypothetical probabilities
"""


import numpy as np
intersection_module = __import__('1-intersection')


def marginal(x, n, P, Pr):
    """
    calculates the marginal probability of obtaining
    the data given various hypothetical probabilities
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(("x must be an integer that is"
                          "greater than or equal to 0"))
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Calculate the intersection (Likelihood * Prior) for each P
    intersection_values = intersection_module.intersection(x, n, P, Pr)

    # Marginal probability is the sum of the intersection values
    marginal_probability = np.sum(intersection_values)

    return marginal_probability
