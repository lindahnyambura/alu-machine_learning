#!/usr/bin/env python3

"""
This module contains the class Poisson for modeling Poisson distributions
"""


class Poisson:
    """
    Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        initialization of class
        """

        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")

        if data is None:
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        calculates the value of the PMF for a given number of successes
        """

        k = int(k)
        if k < 0:
            return 0

        # calculate the pmf
        lambtha = self.lambtha
        e = 2.7182818285
        pmf_value = ((lambtha ** k) * (e ** -lambtha)) / self.factorial(k)

        return pmf_value

    def factorial(self, n):
        """
        calculates the factorial of a given number
        """

        n = int(n)
        if n == 0 or n == 1:
            return 1

        # calculate the factorial
        factorial_value = 1
        for i in range(2, n + 1):
            factorial_value *= i

        return factorial_value
