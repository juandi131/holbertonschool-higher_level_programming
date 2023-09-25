#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx >= len(my_list) or idx < 0:
        return my_list.copy()
    a = 0
    while a <= (len(my_list) - 1):
        new_list.append(my_list[a])
        a += 1
    new_list[idx] = element
    return (new_list)
