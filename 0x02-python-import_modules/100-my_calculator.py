#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    opt = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in opt.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = opt[sys.argv[2]](a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
