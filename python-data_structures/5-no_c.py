#!/usr/bin/python3
# -*- coding: utf-8 -*-
def no_c(my_string):
    result = ""  # Nəticəni saxlayacağımız boş bir 
    for char in my_string:  # Verilən sətirdəki hər bir xarakteri yoxlay
        if char != 'c' and char != 'C':  # Əgər xarakter 'c' və ya 'C' deyil
            result += char  # O zaman onu nəticəyə əlavə ed
    return result  # Yeni sətiri qaytarır�
