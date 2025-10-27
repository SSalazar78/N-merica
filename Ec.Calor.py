# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 15:29:50 2025

@author: Susana A.S.R

Ecuación del calor por diferencias finitas
"""
import numpy as np
import matplotlib.pyplot as p

#Condiciones iniciales

L = 1 #Longitud de la barra en metros 
t = 10000 
ts = 6000
n = 50 #Pasos espaciales
K = 237 #Coductividad termica del aluminio
C = 900 #Capacidad calorifica del aluminio
rho = 2700 #Densidad del aluminio


#Discretización

DX = L/(n-1)

DT = ts/t 

eta = ((K/(C*rho))*DT)/(DX**2) #Condición de Neumann

if eta < 0.5:
    print("La aproximación por el método de diferenciación finita será buena")
else:
    print("La aproximación por el método de diferenciación finita no será buena")
    
#Inicialización de una matriz de ceros con tamaño t+1 y n+1
#Filas = Tiempo , Columnas = Posición
T = np.zeros((t+1, n+1))

#Ingresamos la temperatura inicia con excepción en los extremos
for i in range(1,n-1): #Vamos punto por punto hasta un paso antes de llegar al extremo
    T[0,i] = 100
    
#Llenado de la matriz con los t y n 

for j in range(0, t):        # Paso en el tiempo
#Imponiendo las condiciones de frontera
    T[j,0] = 0  #Temperatura en el extremo x = 0
        
    T[j,n] = 0  #Temperatura en el extremo x = L
    
    for i in range(1, n):    # Paso en el espacio
        T[j+1, i] = T[j, i] + eta*(T[j, i+1] + T[j, i-1] - 2*T[j, i])

#Parte gráfica en 3D

#Discretizar las coordenadas x y t
x = np.arange(n+1)
x = x * DX #Multiplicamos cada i en el arreglo x por DX

y = np.arange(t+1)  
y = y * DT #Multiplicamos cada i en el arreglo y por DT

# la malla hecha con los puntos de la matriz T
X, Y = np.meshgrid(x, y)

fig = p.figure()

ax = fig.add_subplot(111, projection='3d')  #Una sola figura, una sola columna, primer subplot

ax.set_ylabel("Distancia (m)")
ax.set_xlabel("Tiempo (s)")
ax.set_zlabel("Temperatura (°C)")
ax.set_title('Temperatura en una barra de aluminio, método de diferencias finitas')

sup = ax.plot_surface(Y, X, T, cmap='hot', linewidth=0)

ax.set_xlim(0, 6001)
ax.set_ylim(-0.5, 1.3)
ax.set_zlim(0, 130)
fig.colorbar(sup)
p.show()

