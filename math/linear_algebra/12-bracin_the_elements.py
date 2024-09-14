#!/usr/bin/env python3
import numpy as np

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): The first array.
        mat2 (numpy.ndarray or int/float): The second array or a scalar.

    Returns:
        tuple: A tuple containing the element-wise sum, difference, product, and quotient.
    """
    return (np.add(mat1, mat2), np.subtract(mat1, mat2), np.multiply(mat1, mat2), np.divide(mat1, mat2))
