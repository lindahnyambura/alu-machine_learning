#!/usr/bin/env python3
"""
class RNNcell that represents a cell of a simple RNN
"""


import numpy as np


class RNNCell:
    """
    class that represents a cell of a simple RNN
    """

    def __init__(self, i, h, o):
        """
        class constructor
        """
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))
        self.Wh = np.random.normal(size=(h + i, h))
        self.Wy = np.random.normal(size=(h, o))

    def softmax(self, x):
        """
        softmax function
        """
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        softmax = e_x / np.sum(e_x, axis=1, keepdims=True)
        return softmax
    
    def forward(self, h_prev, x_t):
        """
        performs forward propagation for one time step
        """
        concat = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.matmul(concat, self.Wh) + self.bh)
        y = self.softmax(np.matmul(h_next, self.Wy) + self.by)
        return h_next, y
