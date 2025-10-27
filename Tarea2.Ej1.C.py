# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 19:12:14 2025

@author: Susana A.S.R
"""


#Inciso 1.C

#Definimos la función sin la corrección 
def c1(x,y):
    return(x**2 - y**2)

#Definimos la función con la corrección para evitar la cancelación
def c2(x,y):
    return((x-y)*(x+y))

#Pedimos el valor de x
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))


#Imprimimos los resultados de ambas funciones

print("Resultado usando la función original: ", c1(x,y))
print("Resultado con la función que evita la cancelación sustractiva: ", c2(x,y))


