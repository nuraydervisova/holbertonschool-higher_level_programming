#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Eğer liste boş
        return None
    max_num = my_list[0]  # Başlangıçta listenin ilk elemanını en büyük olarak kabu
    for num in my_list:  # Listenin her elemanını kontrol 
        if num > max_num:
            max_num = num  # Daha büyük bir sayı bulunduysa, onu yeni en büyük sayı olar
    return max_num  # En büyük sayıyı d�
