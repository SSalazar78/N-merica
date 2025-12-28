# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 08:29:49 2025

@author: Susana A.S.R
"""
import matplotlib.pyplot as plt

a = 57
c = 1
M = 256
x0 = 10
n = 258 #Cantidad de números a generar

numeros = [] # Para guarda los números generados

x = x0 #Inciamos con la semilla antes del bucle

while True:
    x = (a * x + c) % M
    
    if x in numeros:
        # Busca dónde apareció por primera vez
        p = len(numeros) - numeros.index(x)
        break 
    numeros.append(x)
    
   
print("Números generados:", numeros)
print('Periodo:', p)
   
#Gráfica de los pares (x2i-1, x2i)
#Creación de los arreglos
x = []
y = []

#Se toman pares saltando de 2 en 2
for i in range(0, len(numeros)-1, 2):
    x.append(numeros[i])
    y.append(numeros[i+1])

plt.figure()
plt.scatter(x, y)
plt.title("Pares (x2i−1 , x2i)")
plt.xlabel("x2i−1")
plt.ylabel("x2i")
plt.grid(True)
plt.show()

#Gráfica xi vs i
plt.figure()
plt.scatter(range(len(numeros)), numeros, marker='o')
plt.title('Gráfica xi vs i')
plt.xlabel("xi")
plt.ylabel("i")
plt.grid()
plt.show()
    