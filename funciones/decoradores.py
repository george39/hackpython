#_*_ coding: utf8 _*_


class prueba1(object):
    def __init__(self, radio):
        self.radio = radio

    @classmethod #nos ayuda a usar una funcion sin que antes la clase sea abribuida a un objeto
                #no necesito convertir la clase en un objeto para usar la funcion
    def saludo(cls, nombre):
        print("Hola {}".format(nombre)) 


    @staticmethod #permite usar una funcion sin parametro
    def saludo_static():
        print("Bienvenido")  


    @property #nos permite trabajar con funciones como si fueran variables
     def area_circulo(self):
         return 3.1416(self.radio**2)    


def main():
    nombre = raw_input("NombreS: ") 
    c = prueba1(5)
    area = c.area_circulo
    print(area)                

if if __name__ == "__main__":
    main()    