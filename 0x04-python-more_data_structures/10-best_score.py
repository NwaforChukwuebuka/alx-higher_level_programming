#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    new_list = list(a_dictionary.keys())
    k = new_list[0]
    biggest = a_dictionary[k]
    for key, val in a_dictionary.items():
        if val > biggest:
            biggest = val
            k = key
    return (k)
