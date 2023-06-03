#!/usr/bin/python3
import random
number1 = 0
number = random.randint(-10000, 10000)
number1 = number % 10
if number1 > 5:
    print(f"Last digit of {number} is {number1} is greater than 5 and not 0")
elif number != 0 and number < 6:
    print(f"Last digit of {number} is {number1} is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
