#!/usr/bin/env python
#_*_ coding: utf8: _*_


#diccionario vacio
dic = {}
diccionario = dict(nombre='alumno', plataforma='udemy', edad=43)
print(diccionario['nombre'])

#copiar un diccionario
b = diccionario.copy()

print(b)

#mostrar una posicion de un diccionario
for n in diccionario.keys():
    print("{} Su valor es: {}".format(n, diccionario[n]))