#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide
if __name__ == "__main__":
    a = 10
    b = 5
    # Funksiyaları çağırırıq
    result_add = add(a, b)
    result_subtract = subtract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)
    # Nəticələri çap edirik
    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_subtract))
    print("{} * {} = {}".format(a, b, result_multiply))
    print("{} // {} = {}".format(a, b, result_divide))
