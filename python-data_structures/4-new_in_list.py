#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list"""
    if idx < 0 or idx >= len(my_list):
        # Check if the index is out of range or negative
        return my_list.copy()  # Return a copy of the original list
    new_list = my_list.copy()  # Create a copy of the original list
    new_list[idx] = element  # Replace the element at the specific index
    return new_list  # Return the modified copy
