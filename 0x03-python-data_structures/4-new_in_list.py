#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    updated_list = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return (updated_list)
    updated_list[idx] = element
    return (updated_list)
