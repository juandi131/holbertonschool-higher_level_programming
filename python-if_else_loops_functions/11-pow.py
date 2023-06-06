#!/usr/bin/python3
def pow(a, b):
    c = a
    d = b - 1
    for i in range(d):
        c = c * a
    return c
