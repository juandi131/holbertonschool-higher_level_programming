#!/usr/bin/python3
str = "seXonFus"
for letter in str:
    if ord(letter) >= 97 and ord(letter) <= 122:
        letter = chr(ord(letter) - 32)
    print(f"{letter}", end="")
print("")