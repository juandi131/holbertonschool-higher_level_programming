#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for elements in a_dictionary:
        a_dictionary[elements] = a_dictionary[elements] * 2
        return (a_dictionary[elements])
