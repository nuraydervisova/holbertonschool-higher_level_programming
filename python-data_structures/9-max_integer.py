#!/usr/bin/python3
def max_integer(my_list=[]):
    # Əgər siyahı boşdursa, None qaytar
    if len(my_list) == 0:
        return None
    # Siyahını sətir-sətir nəzərdən keç
    largest = my_list[0]  # İlk elementi ən böyük ədəd olaraq təyin
    for num in my_list:
        if num > largest:
            largest = num  # Yeni ən böyük ədəd tapıldıqda onu təyi
    return largest
