#!/usr/bin/python3

for i in range(97, 123):  # ASCII dəyərləri 97-122 (a-dan z-yə)
    if i <= 105:  # 79 simvola bölmək üçün iki sətirə ayırırıq
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i)), end="")
