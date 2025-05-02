#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Siyahı boşdur
        return None
    max_num = my_list[0]  # İlk elementi ən böyük olaraq qəb
    for num in my_list:  # Siyahı üzərində hər bir elementi yoxla
        if num > max_num:
            max_num = num  # Əgər daha böyük bir element tapsaq, onu ən böyük kimi tt
    return max_num
