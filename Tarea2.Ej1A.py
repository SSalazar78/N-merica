# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 18:51:54 2025

@author: Susana A.S.R
"""

import numpy as n #Importamos la biblioteca necesaria

#Inciso 1.A

#Definimos la función sin la corrección 
def a1(x):
    return((n.sqrt(x + 1) - 1))

#Definimos la función con la corrección para evitar la cancelación
def a2(x):
    return(x/((n.sqrt(x+1)) + 1))

#Pedimos el valor de x
x = float(input("Ingrese el valor de x: "))

#Imprimimos los resultados de ambas funciones

print("Resultado usando la función original: ", a1(x))
print("Resultado con la función que evita la cancelación sustractiva: ", a2(x))

""" A pesar de que en apariencia los resultados son los mismos cuando x tiende a cero,
La diferencia radica en cómo es que ese cero aparece."""

