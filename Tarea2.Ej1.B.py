# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 19:09:08 2025

@author: Susana A.S.R
"""
import numpy as n #Importamos la biblioteca necesaria
import math as m
#Inciso 1.B

#Definimos la función sin la corrección 
def b1(x,y):
    return(n.sin(x)-n.sin(y))

#Definimos la función con la corrección para evitar la cancelación
def b2(x,y):
    return(2*n.cos((x+y)/2) * n.sin((x-y)/2))

#Pedimos el valor de x
x = float(input("Ingrese el valor de x en grados: "))
y = float(input("Ingrese el valor de y en grados: "))

#Convertir los grados ingresados en radianes
x1 = x * (m.pi/180.0)

y1 = y * (m.pi/180.0)

#Imprimimos los resultados de ambas funciones

print("Resultado usando la función original: ", b1(x1,y1))
print("Resultado con la función que evita la cancelación sustractiva: ", b2(x1,y1))
