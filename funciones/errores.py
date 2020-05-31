#1/usr/bin/env python 
#_*_ coding: utf8 _*_


try:
    while True:
        print("hola")

except NameError:
    print('l no esta definida') 

except NameError:
    print('Salida forzosa')           

finally:
    print('Termino la ejecucion')  



#generar nuestros propios errores
try:
    raise IOError
except  IOError:
    print('Ocurrio un error')     