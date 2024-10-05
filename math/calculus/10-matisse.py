#!/usr/bin/env python3

"""Matisse's method to calculate the derivative of a polynomial."""

def poly_derivative(poly):
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    
    if len(poly) == 1:
        return [0]
    
    derivative = [coef * i for i, coef in enumerate(poly) if i > 0]
    
    return derivative if derivative else [0]
