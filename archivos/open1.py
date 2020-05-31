#1/usr/bin/env python 
#_*_ coding: utf8 _*_


archivo = open("archivo.txt", "w")
nombre = raw_input("Nombre: ")
edad = raw_input("edad: ")
pais = raw_input("pais: ")

print("He escrito los datos")
archivo.close()