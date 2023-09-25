#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 0
    resultado = 1
    if len(argv) == 1:
        print("0")
    for a in argv:
        if n == 0:
            n += 1
            continue
        resultado = resultado + int(a)
    print("{}".format(resultado))
