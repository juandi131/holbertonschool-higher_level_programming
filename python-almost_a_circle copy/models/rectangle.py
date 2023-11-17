#!/usr/bin/python3
"""Task 2"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        sexo = {'width': width, 'height': height, 'x': x, 'y': y}
        for a, l in sexo.items():
            if not isinstance(l, int):
                raise ValueError(f"Invalid value for {a}")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
            if not isinstance(value, int):
                raise ValueError("Width must be an integer")
            if value <= 0:
                raise ValueError("` Width must be > 0")
                self.__width = value
        
    @property
    def height(self):
            return self.__height
        
    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__Y
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("Height must be an integer")
        if value <= 0:
             raise ValueError("height must be > 0")
        self.__height = value

