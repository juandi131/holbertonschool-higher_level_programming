#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = [1, 2, 5, 7, 8]
    idx = 3
    element = 0
    new_list = []
    if idx >= len(my_list) or idx < 0:
        return my_list
    a = 0
    while a <= (len(my_list) - 1):
        new_list.append(my_list[a])
        a += 1
    new_list[idx] = element
    return (new_list)
