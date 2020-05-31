#!/usr/bin/env python
#_*_ coding: utf8 _*_


lista = [1,2,3,4,5,62,"a", "b", 2.1, True]
for i in lista:
    print(i)


print(lista[len(lista) -1])   #muestra el ultimo elemento de la lista

#elimina el ultimo elemento de la lista
lista.pop()

#elimina una posicion de una lista
del lista[1]

#imprime de la una posicion hasta otro posicion especifica
print(lista[0:10])

#añadir valores a una lista
for n in range(90,100):
    lista.append(n)

#convertir una lista a una cadena de texto
lista = ['h','o','l','a']
lista = ''.join(lista)     