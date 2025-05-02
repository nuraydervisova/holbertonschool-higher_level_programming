#!/usr/bin/python3
def add(a, b):
    """Return the sum of a and b."""
    return a + b
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
def divide(a, b):
    """Return the quotient of a and b as an integer."""
    if b == 0:
        return "Error: Division by zero"
    return a // b  # Tam bölmə (integer division)
