#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Yeni bir matrix yaratmaq üçün list comprehension istifadə ed
    return [[x**2 for x in row] for row in matrix]
