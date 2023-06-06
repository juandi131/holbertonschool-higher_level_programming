#!/usr/bin/python3
def fizzbuzz():
for i in range(1, 101):
    a = i % 3
    if a == 0:
        print("fizz ", end="")
    else:
        print(f"{i} ", end="")
print()
