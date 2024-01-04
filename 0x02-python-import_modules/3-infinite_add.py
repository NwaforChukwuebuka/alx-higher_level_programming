#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all args."""
    import sys

    sum = 0
    args_count = len(sys.argv)
    for x in range(args_count - 1):
        sum += int(sys.argv[x + 1])
    print("{}".format(sum))
