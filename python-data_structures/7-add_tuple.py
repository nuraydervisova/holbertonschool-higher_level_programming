#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Doldurulması lazımdırsa, tuple-ları 2 elementli et
    tuple_a = tuple_a + (0, 0)  # Tuplenin uzunluğu 2-dən azsa, 0 əlavə e
    tuple_b = tuple_b + (0, 0)  # Eyni şəkildə
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
