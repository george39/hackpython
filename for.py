#!/usr/bin/env python
#_*_ coding: utf8 _*_

numero = int(raw_input('Numero'))
mensaje = raw_input('Mensaje')



for i in range(0,numero):
    print("{} = {}".format(i,mensaje))