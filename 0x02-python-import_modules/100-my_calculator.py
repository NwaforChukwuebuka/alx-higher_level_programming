#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic ops."""
    from calculator_1 import add, sub, mul, div
    import sys
    args_count = len(sys.argv)
    if args_count - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operation = operators[sys.argv[2]]
    print("{} {} {} = {}".format(a, sys.argv[2], b, operation(a, b)))
