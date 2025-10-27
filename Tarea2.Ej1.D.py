# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 19:19:51 2025

@author: Susana A.S.R
"""
import numpy as n #Importamos la biblioteca necesaria
import math as m

#Inciso 1.D

#Definimos la función sin la corrección 
def d1(x):
    return((1 - n.cos(x))/n.sin(x))

#Definimos la función con la corrección para evitar la cancelación
def d2(x):
    return(n.tan(x/2))

#Pedimos el valor de x
x = float(input("Ingrese el valor de x en grados: "))

#Convertir los grados ingresados en radianes
x1 = x * (m.pi/180.0)

#Imprimimos los resultados de ambas funciones

print("Resultado usando la función original: ", d1(x1))
print("Resultado con la función que evita la cancelación sustractiva: ", d2(x1))

"""En este caso, cuando ingresamos x=0, el resultado que regresa
la función sin la modificación es nan (not a number ), porque estamos 
diviendo entre cero."""