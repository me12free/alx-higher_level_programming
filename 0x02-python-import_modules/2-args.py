#!/usr/bin/python3
import sys

if __name__ == "__main__":

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("{} argument:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
    else:
        print("{} arguments:".format(count))

        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
