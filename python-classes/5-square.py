#!/usr/bin/python3
""" cuadrado cuadrado"""


class Square:
    """ texto texto"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ comentario"""
        return self.__size

    @size.setter
    def size(self, value):
        """ comentario """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area de cuadradp """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
