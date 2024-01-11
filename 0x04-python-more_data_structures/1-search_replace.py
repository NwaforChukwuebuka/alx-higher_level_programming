#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for ele in range(len(new_list)):
        if new_list[ele] == search:
            new_list[ele] = replace
    return (new_list)
