#!/usr/bin/python3
import sys
import hidden_4  # hidden_4.pyc faylını import edirik
if __name__ == "__main__":
    # hidden_4 modulunun bütün atributlarını alırıq
    names = dir(hidden_4)
    # '__' ilə başlamayan adları seçirik
    filtered_names = [name for name in names if not name.startswith('__')]
    # Adları əlifba sırasına görə sıralayırıq
    filtered_names.sort()
    # Adları bir-bir çap edirik
    for name in filtered_names:
        print(name)
