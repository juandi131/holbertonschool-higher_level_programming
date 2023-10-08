#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # ... Other methods and properties ...

    def __del__(self):
        print("Bye rectangle...")

# Create an instance of Rectangle
rect = Rectangle(5, 10)

# Delete the instance (this will trigger the __del__ method)
del rect
