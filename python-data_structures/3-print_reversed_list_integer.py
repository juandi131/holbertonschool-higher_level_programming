#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
my_list = [1, 5, 7, 8, 6]
for i in range(len(my_list) -1, -1, -1):
     print("{}".format(my_list[i]))
