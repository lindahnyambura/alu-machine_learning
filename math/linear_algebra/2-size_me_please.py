#!/usr/bin/env python3
"""Size Me Please."""

def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
