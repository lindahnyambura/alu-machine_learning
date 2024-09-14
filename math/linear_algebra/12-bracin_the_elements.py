#!/usr/bin/env python3
"""Bracin The Elements."""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): The first array.
        mat2 (numpy.ndarray): The second array.

    Returns:
        tuple: A tuple containing the element-wise sum, difference,
        product, and quotient.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
