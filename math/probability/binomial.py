#!/usr/bin/env python3

"""
This module contains the class Binomial for
modeling binomial distributions
"""


class Binomial:
    """
    Binomial class for modeling binomial distributions
    """

    def __init__(self, data=None, n=1, p=0.5):
        """Initialization of class
        Args:
            data: list of data to be used for binomial distribution
            n: number of data points
            p: probability of occurence
        """

        if data is None:
            if not isinstance(n, int) or n <= 0:
                raise ValueError("n must be a positive integer")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = float(p)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            
            # calculate the mean
            mean = sum(data) / len(data)

            # calculate the variance
            variance = sum([(x - mean) ** 2 for x in data]) / len(data)

            # estimate p and n based on mean and variance
            self.p = 1 - (variance / mean)
            self.n = round(mean / self.p)

            self.p = mean / self.n
