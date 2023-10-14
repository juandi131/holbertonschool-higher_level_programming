#!/usr/bin/python3
"""task 1"""
import json


class Base():
    """model base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
base1 = Base(sesx)
print(base1.id)