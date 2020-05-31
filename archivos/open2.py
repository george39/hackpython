#1/usr/bin/env python 
#_*_ coding: utf8 _*_


archivo = open('wordlist.lst', 'r')

for l in archivo.read().split('\n'):

    print(l)


lista = archivo.read().split('\n')
for n in lista:
    print(n)

