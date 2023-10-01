#!/usr/bin/python3
cesar = "DCCVII"
a = 0
b = 0
resultado = 0
cadena = []
roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
for a in range(len(cesar)):
    char = cesar[a]
    for car in roman_dict:
        if char == car:
            lol = roman_dict.get(car)
            cadena.append(lol)
            print(cadena)
resultado = cadena[len(cadena) - 1]
for i in range(len(cadena) - 1, -2, -1):
    if cadena[i] > cadena[i - 1]:
        resultado = resultado - cadena[i - 1]
    else:
        resultado = resultado + cadena[i - 1]
print(resultado)
