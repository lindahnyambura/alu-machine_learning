#!/usr/bin/env python3
"""
Write a Python program that calculates the
summation of all the elements in a list
"""


def summation_i_squared(n):
    """Calculates the summation of all
    the elements in a list."""
    if not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
