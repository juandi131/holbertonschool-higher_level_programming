#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a = dict()
    for a in a_dictionary:
        new_a.update({a: a_dictionary[a] * 2})
    return new_a