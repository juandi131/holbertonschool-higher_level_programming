#!/usr/bin/python3
for i in range(1, 101):
    a = i % 3
    d = i % 5
    if a == 0 and d == 0:
        print("FizzBuzz ", end="")
    elif a == 0:
        print("Fizz ", end="")
    elif d == 0:
        print("Buzz ", end="")
    else:
        print(f"{i} ", end="")
print()
