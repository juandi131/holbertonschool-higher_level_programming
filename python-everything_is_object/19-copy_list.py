#!/usr/bin/python3class MiClase:
class MiClase:
    def obtener_atributos(self):
        return dir(self.__dir__)

objeto = MiClase()
print(objeto.obtener_atributos())