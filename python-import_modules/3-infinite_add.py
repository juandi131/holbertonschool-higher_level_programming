#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    resultado = 0
    for a in argv[1:]:
        resultado += int(a)

    print("{}".format(resultado))
