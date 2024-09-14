#!/usr/bin/env python3
"""Flip Me Over."""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of list of int/float): A 2D matrix to be transposed.

    Returns:
        list of list of int/float: The transposed matrix.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
