#!/usr/bin/env python
#_*_ coding: utf8 _*_

# def saludo():
#     print('Bienvenida')


# def despedidia():
#     print('Adios')


# def main():
#     saludo()
#     despedidia()


def saludo(nombre, edad):
    print('hola {} tienes: {}'.format(nombre, edad))


def main():
    nombre = raw_input("Nombre: ")
    edad = int(raw_input("edad: "))
    saludo(nombre, edad)    

if __name__ == '__main__':
    main()