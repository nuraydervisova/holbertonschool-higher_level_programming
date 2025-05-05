#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # List comprehension istifadə edərək, hər bir elementi yoxlayırıq
    return [replace if x == search else x for x in my_list]
