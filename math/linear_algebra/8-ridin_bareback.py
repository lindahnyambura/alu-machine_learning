#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
        mat1 (list of list of int/float): The first 2D matrix.
        mat2 (list of list of int/float): The second 2D matrix.

    Returns:
        list of list of int/float: A new 2D matrix containing the product of mat1 and mat2.
        None: If the matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]
    return result
