#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = 0
    s = 0
    for nums in argv:
        if s != 0:
            a += int(nums)
        s = 1
    print("{}".format(a))
