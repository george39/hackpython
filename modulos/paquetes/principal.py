#!/usr/bin/env python
#_*_ coding: utf8 _*_

from paquete1 import calculadora_modulo


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
            calculadora_modulo.sumar(valor1, valor2)

        if opcion == 2:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            calculadora_modulo.restar(valor1, valor2)


        if opcion == 3:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            calculadora_modulo.dividir(valor1, valor2)


        if opcion == 4:
            valor1 = int(raw_input("Valor 1: "))
            valor2 = int(raw_input("Valor 2: "))
            calculadora_modulo.multiplicar(valor1, valor2)   


        if opcion == 5:
            exit()

        if opcion > 5:
            print("\nOpcion invalida\n") 



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nSliendo...')    