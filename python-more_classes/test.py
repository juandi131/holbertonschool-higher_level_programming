class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # ... Otros métodos y propiedades ...

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

# Crear una instancia de Rectangle
rect = Rectangle(5, 10)

# Utilizar __repr__ para obtener la representación en cadena del objeto
repr_str = repr(rect)

# Imprimir la representación en cadena
print(repr_str)