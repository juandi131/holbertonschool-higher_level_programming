#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letterupper = chr(ord(letter) - 32)
            print(f"{letterupper}", end="")
        else:
            print(f"{letter}", end="")
    print("")
