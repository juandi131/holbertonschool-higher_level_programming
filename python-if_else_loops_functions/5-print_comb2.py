#!/usr/bin/python3
for a in range(10):
    for d in range(a + 1, 10):
        print("{:d}{:d}".format(a, d), end=", " if not (a == 8 and d == 9) else "\n")
