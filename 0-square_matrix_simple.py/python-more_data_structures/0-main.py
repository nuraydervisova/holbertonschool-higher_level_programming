#!/usr/bin/python3
# -*- coding: utf-8 -*-
# square_matrix_simple funksiyasını import edirik
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
# Test matrisi
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# square_matrix_simple funksiyasını çağırıb yeni matrix əld�k
new_matrix = square_matrix_simple(matrix)
# Nəticələri çap edirik
print(new_matrix)  # Yeni matrix: kvadratlar
print(matrix)      # Əsl matrix: dəyişməz q
