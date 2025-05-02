#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # idx mənfi və ya siyahıdan kənarda olduqda, orijinal siyahının kopyasını qaytarır
    new_list = my_list.copy()  # Orijinal siyahını kopyalayır
    new_list[idx] = element  # Kopyalanmış siyahıda elementi dəyişdirir
    return new_list  # Dəyişdirilmiş siyahını qaytarır
