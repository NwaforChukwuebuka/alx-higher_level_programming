#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    int_printed = 0
    try:
        for i in range(x):
            try:
                print(f"{my_list[i]:d}", end="")
                int_printed += 1
            except (TypeError, ValueError):
                pass

    except IndexError:
        pass

    print()
    return (int_printed)
