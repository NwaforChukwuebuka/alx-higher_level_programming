#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    num_of_ele_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            num_of_ele_printed += 1

    except IndexError as IE:
        pass

    print("")
    return (num_of_ele_printed)
