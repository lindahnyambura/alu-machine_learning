#!/usr/bin/env python3
""" 17-integrate.py """

def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    if not isinstance(C, (int, float)):
        return None
    
    integral = [C]  # Start with the integration constant
    for i, coef in enumerate(poly):
        integral.append(coef / (i + 1))
    
    # Convert coefficients to integers if they are whole numbers
    integral = [int(coef) if coef.is_integer() else coef for coef in integral]
    
    return integral
