#!/usr/bin/env python3

"""
This module contains the class Normal for
modeling normal distributions
"""


class Normal:
    """
    represents a normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        initialization of class
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = float(sum(data) / len(data))
            self.mean = float(mean)
            self.stddev = float(self.calculate_stddev(data, self.mean))

    def calculate_stddev(self, data, mean):
        """
        calculates the standard deviation
        """
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return (variance ** 0.5)

    def z_score(self, x):
        """
        calculates the z-score
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        calculates the x-value
        """
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """
        calculates the value of the PDF for a given number
        """
        if self.stddev <= 0:
            return 0
        exponent = -((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        coefficient = 1 / (self.stddev * (2 * 3.1415926536) ** 0.5)
        return coefficient * (2.7182818285 ** exponent)

    def cdf(self, x):
        """
        calculates the value of the CDF for a given number
        """
        z = self.z_score(x)
        t = z - (z ** 3) / 3 + (z ** 5) / 10 - (z ** 7) / 42 + (z ** 9) / 216
        cdf = 0.5 * (1 + (2 / (3.1415926536 ** 0.5)) * t)
        return cdf
