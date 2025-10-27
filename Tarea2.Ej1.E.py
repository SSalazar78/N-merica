# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 19:26:26 2025

@author: Susana A.S.R
"""

import numpy as n #Importamos la biblioteca necesaria
import math as m

#Inciso 1.E

#Definimos la función sin la corrección 
def e1(a,b,x):
    return(n.sqrt(a**2 + b**2 - (2*a*b*n.cos(x))))

#Definimos la función con la corrección para evitar la cancelación
def e2(a,b,x):
    return(n.sqrt((a-b)**2 + 4*a*b*(n.sin(x/2)**2)))

#Pedimos el valor de x
a = float(input("Ingrese el valor de a : "))
b = float(input("Ingrese el valor de b : "))
x = float(input("Ingrese el valor de x en grados: "))

#Convertir los grados ingresados en radianes
x1 = x * (m.pi/180.0)

#Imprimimos los resultados de ambas funciones

print("Resultado usando la función original: ", e1(a,b,x1))
print("Resultado con la función que evita la cancelación sustractiva: ", e2(a,b,x1))
