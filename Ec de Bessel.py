# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 10:22:24 2025

@author: Susana A.S.R
"""

#Ejercicio ec bessel

#Importamos la libreria necesaria y la funcion de bessel para definir valores iniciales
from scipy.special import spherical_jn
import numpy as n

#Algoritmo hacia arriba
#Definimos la funcion mediante recursion
def Jup(x,l):
    ju = n.zeros(l+2) #Creacion de una array para guardar los valores

    #Valores iniciales de J
    ju[1] = n.sin(x)/(x**2) - n.cos(x)/x
    ju[0] = n.sin(x)/x

    # Recurrencia hacia arriba
    for i in range(1, l, 1): #Iniciamos en 1, paramos cuando i = l, y vamos de 1 en 1
        ju[i+1] = ((2*i+1)/x) * ju[i] - ju[i-1]

    return ju[l]


#Algoritmo hacia abajo (metodo de Miller)
def Jdn(x,l):
    jd = n.zeros(l+2) #Creacion de un array

    jd[l+1] = spherical_jn(l + 1, x) #calcula la funion de bessel de orden l+1
    jd[l] = spherical_jn(l,x)#calcula la funcion de bessel de orden l


    # Recurrencia hacia abajo
    for i in range(l, 0, -1): #Iniciamos en l, paramos cuando l = 0, y vamos de -1 en -1
      jd[i-1] = ((2*i+1)/x) * jd[i] - jd[i+1]

    # Normalización con j0(x) exacto segun el algoritmo de Miller
    j0_e = n.sin(x)/x
    factor = j0_e / jd[0]
    jd *= factor

    return jd[l]

#Array para los tres valores de x a evaluar
x = n.array([0.1,1,10])

#Imprimir los resultados
for i in x:
    print(f'En x={i}') #Hacemos una fila para cada uno de los tres valores de x
    print(f"{'l':<10}{'Down':<25}{'Up':<25}{"Diferencia":<25}") #imprimir cadenas alineadas con 25 caracteres por columna

    for j in range(0,25):
      #Guardan los valores evaluados en nuevas variables
      BU = Jup(i,j)
      BD = Jdn(i,j)
      E = abs(BU-BD)/(abs(BU) + abs(BD))
      print(f"{j:<10}{BD:<25e}{BU:<25e}{E:<25}") #Imprime los 25 primero valores de la funcion y la diferencia entre ambos metodos para cada x

