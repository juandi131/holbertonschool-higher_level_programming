#!/usr/bin/python3
for i in range(0, 100):  
    if i >= 0 and i < 10:
        print("0{}, ".format(i), end='')
        continue
    if i == 99:
        print("{}".format(i))
        break
    print("{} ,".format(i), end='')
