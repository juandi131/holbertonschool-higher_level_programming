#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return None
    resultado = 0
    cadena = []
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Convertir números romanos a una lista de valores
    for char in cesar:
        if char in roman_dict:
            valor = roman_dict[char]
            cadena.append(valor)

    # Calcular el resultado sumando los valores
    for i in range(len(cadena)):
        if i < len(cadena) - 1 and cadena[i] < cadena[i + 1]:
            resultado -= cadena[i]
        else:
            resultado += cadena[i]

    print(resultado)
    