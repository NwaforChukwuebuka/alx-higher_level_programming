#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    weight = 0
    avg_wt = 0
    for tuple in my_list:
        avg_wt += (tuple[0] * tuple[1])
        weight += tuple[1]
    return (avg_wt / weight)
