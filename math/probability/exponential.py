#!/usr/bin/env python3

"""
This module contains the class Exponential for
modeling exponential distributions
"""


class Exponential:
    """
    representing an exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        initialization of class
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(1/ sum(data) / len(data))