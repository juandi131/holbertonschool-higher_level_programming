#!/usr/bin/python3
""" ints from """


def inherits_from(obj, a_class):
    """ is from """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
    