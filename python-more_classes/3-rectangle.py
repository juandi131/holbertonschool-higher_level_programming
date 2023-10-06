#!/usr/bin/python3
"""Task 0"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.__height * self.__width
        return area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            perimeter = self.__height * 2 + self.__width * 2
            return perimeter

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        for a in range(self.__height):
            print("")
            for c in range (self.width):
                print("#", end="")

