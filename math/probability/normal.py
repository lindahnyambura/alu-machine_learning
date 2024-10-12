#!/usr/bin/env python3
"""
This module contains the class Normal for
modeling normal distributions
"""


class Normal:
    """
    representing a normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        initialization of class
        """

        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            stddev_num = [(x - self.mean) ** 2 for x in data]
            self.stddev = (sum(stddev_num) / len(data)) ** 0.5

    def z_score(self, x):
        """
        returns the z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        returns the x-value of z
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        '''
        returns the pdf
        '''
        exponent = -((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        pdf_value = (1 / (self.stddev * ((2 * 3.1415926536) ** 0.5))) * \
            (2.7182818285 ** exponent)
        return pdf_value

    def cdf(self, x):
        '''
        returns the cdf
        '''
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        t = z - (z ** 3) / 3 + (z ** 5) / 10 - (z ** 7) / 42 + (z ** 9) / 216
        cdf = 0.5 * (1 + (2 / (3.1415926536 ** 0.5)) * t)
        return cdf
