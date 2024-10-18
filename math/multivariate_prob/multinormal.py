#!/usr/bin/env python3

"""
calculates the mean and covariance matrix of a data set
"""


import numpy as np


class MultiNormal:
    """
    repesents a multivariate normal distribution
    """

    def __init__(self, data):
        """
        initializes the multivariate normal distribution
        """

        # 2D (RIP Liam)
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        # 2 data points
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # mean
        self.mean = np.mean(data, axis=1, keepdims=True)

        # center data by subtracting mean
        X_centered = data - self.mean

        # covariance matrix
        self.cov = (X_centered @ X_centered.T) / (n - 1)
