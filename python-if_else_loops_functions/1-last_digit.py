#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number}", end="")
if number < 0:
    lastnumber = number % -10
elif number > 0:
    lastnumber = number % 10
if lastnumber > 5:
    print(f" is {lastnumber} and is greater than 5")
elif lastnumber < 6 and lastnumber != 0:
    print(f" is {lastnumber} and is less than 6 and not 0")
elif number == 0:
    print(f" is 0 and is 0")
