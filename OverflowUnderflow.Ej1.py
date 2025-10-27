# -*- coding: utf-8 -*-
"""
Ejercicio 1. Determinar el Underflow
y Overflow con un factor de 2.

"""
#Hay que hacer un while para que se repita la dvisión
#Hay que romper el while cuando el número ya sea indestingible de 0.0
#para la maquina.

def under():
  x = 1.0
  while True:
    bajo = x/2
    if bajo == 0.0:
      print("El underflow es: ", x)
      break;
    x = bajo
under()

#Determinando el Overflow.
def over():
  x = 1.0
  while True:
    alto = x * 2
    if alto == float('inf'):             #En este caso el tope es infinito.
      print("El overflow ocurre después de: ", x)
      break
    x = alto
over()

