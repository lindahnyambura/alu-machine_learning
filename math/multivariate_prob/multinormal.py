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

    def pdf(self, x):
        """
        calculates the pdf of a multivariate normal distribution
        """

        # check if x is a numpy.ndarray
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        # check if x has the right shape
        d, _ = self.mean.shape
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # calculate the pdf
        det_cov = np.linalg.det(self.cov)  # determinant of the covamatrix
        inv_cov = np.linalg.inv(self.cov)  # inverse of the covariance matrix


        # check if the covariance matrix is positive definite
        if det_cov <= 0:
            raise ValueError("Covariance matrix must be positive definite")

        # calculate the normalization constant
        denominator = np.sqrt(((2 * np.pi) ** d) * det_cov)

        # calculate the exponent
        x_centered = x - self.mean
        exponent = np.exp(-0.5 * (x_centered.T @ inv_cov @ x_centered))

        # final pdf value
        pdf = (1 / denominator) * np.exp(exponent)
        return float(pdf)
