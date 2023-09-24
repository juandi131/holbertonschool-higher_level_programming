#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    number = 0
    i = len(argv)
    if i == 1:
        print("{} arguments.".format(i - 1))
    elif i == 2:
        print("{} argument:".format(i - 1))
    else:
        print("{} arguments:".format(i - 1))
    if i > 1:
        for l in argv:
            if number != 0:
                print("{}: {}".format(number, l))
            number = number + 1
