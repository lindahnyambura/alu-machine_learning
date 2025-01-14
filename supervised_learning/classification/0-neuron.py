#!/usr/bin/env python3

"""
Neuron class
This module contains the Neuron class used for machine learning.
"""

import numpy as np

class Neuron:
    """
    Neuron class
    Represents a single neuron performing binary classification.
    """


    def __init__(self, nx):
        """
        Initialize a Neuron instance.

        Parameters:
        nx (int): The number of input features to the neuron.

        Raises:
        TypeError: If nx is not an integer.
        ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
