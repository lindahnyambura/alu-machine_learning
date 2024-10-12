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
                raise ValueError("n must be a positive value")
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

    def pmf(self, k):
        """
        calculates the value of the PMF for a given number of successes
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0

        binomial_coeff = self.binomial_coefficient(self.n, k)

        pmf_value = (binomial_coeff * (self.p ** k) *
                     ((1 - self.p) ** (self.n - k)))

        return pmf_value

    def binomial_coefficient(self, n, k):
        """
        calculates the binomial coefficient
        """
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def factorial(self, n):
        """
        calculates the factorial of a given number
        """
        if n == 0 or n == 1:
            return 1
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    def cdf(self, k):
        """
        calculates the value of the CDF for a given number of successes
        """
        k = int(k)
        if k < 0:
            return 0

        if k > self.n:
            return 1

        cdf_value = sum(self.pmf(i) for i in range(k + 1))

        return cdf_value
