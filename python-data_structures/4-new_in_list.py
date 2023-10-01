#!/usr/bin/python3
#def new_in_list(my_list, idx, element):
from prueba import my_list, idx, element
new_list = []
if idx >= len(my_list) or idx < 0:
    #return my_list
    exit
else:
    e = 0
    for a in my_list:
        if e == idx:
            a = element
        new_list.append(a)
        e = e + 1
    print(new_list)