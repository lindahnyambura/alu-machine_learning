#!/usr/bin/env python3

"""
calculates the mean and covariance matrix of a data set
"""


import numpy as np


def mean_cov(X):
    """
    calculates the mean and covariance matrix of a data set
    """
    # check if X is a 2D array
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    # is the number of data points at least 2?
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # mean
    mean = np.mean(X, axis=0).reshape(1, d)

    # covariance matrix
    X_centered = X - mean
    cov = (X_centered.T @ X_centered) / (n - 1)

    return mean, cov
