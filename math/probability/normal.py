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