#!/usr/bin/env python
#_*_ coding: utf8 _*_


def sumar(valor1, valor2):
    print("La suma es: {}".format(valor1 + valor2) )


def restar(valor1, valor2):
     print("La resta es: {}".format(valor1 - valor2) )


def dividir(valor1, valor2):
     print("La division es: {}".format(valor1 / valor2) )

def multiplicar(valor1, valor2):
     print("La multiplicacion es: {}".format(valor1 * valor2) )


def main():
    while True:
        print("\nBienvenida\n")
        print("1: Suma dos numeros")
        print("2: Resta dos numeros")
        print("3: Divide dos numeros")
        print("4: Multiplica dos numeros")
        print("5: Salir")

        opcion = int(raw_input('Opcion: '))

        if opcion == 1:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            sumar(valor1, valor2)

        if opcion == 2:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            restar(valor1, valor2)


        if opcion == 3:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            dividir(valor1, valor2)


        if opcion == 4:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            multiplicar(valor1, valor2)   


        if opcion == 5:
            exit()

        if opcion > 5:
            print("\nOpcion invalida\n")     

if __name__ == '__main__':
    main()