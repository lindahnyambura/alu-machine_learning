#!/usr/bin/env python3

"""
calculates the correlation matrix from a covariance matrix
"""


import numpy as np

def correlation(C):
    """
    calculates the correlation matrix from a covariance matrix
    """

    # check if C is a numpy.ndarray
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # check if C is a square matrix
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    d = C.shape[0]

    # calculate the stds
    std_devs = np.sqrt(np.diag(C))

    denominator = np.outer(std_devs, std_devs)

    # correlation matrix
    correlation_matrix = C /denominator

    return correlation_matrix
