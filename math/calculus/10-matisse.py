#!/usr/bin/env python3

"""Matisse's method to calculate the derivative of a polynomial."""

def poly_derivative(poly):
    """Returns the derivative of a polynomial."""

    derivative = []

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for i in range(len(poly) - 1):
        derivative.append(poly[i] * (i + 1))
    return derivative
