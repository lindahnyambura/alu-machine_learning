#!/usr/bin/env python3
"""Add two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of list of int/float): The first 2D matrix.
        mat2 (list of list of int/float): The second 2D matrix.

    Returns:
        list of list of int/float: A new 2D matrix containing 
        the element-wise sum of mat1 and mat2.
        None: If mat1 and mat2 are not the same shape.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] 
            for i in range(len(mat1))]
