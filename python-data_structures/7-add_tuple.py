#!/usr/bin/python3
from prueba import *
#def add_tuple(tuple_a=(), tuple_b=()):
list_c = []
lista_a = list(tupla_a)
lista_b = list(tupla_b)
a = 0
for a in range(len(lista_a)):
    list_c.append(lista_a[a] + lista_b[a])
    print(list_c[a])
