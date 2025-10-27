# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 18:04:02 2025

@author: Susana A.S.R
"""
import numpy as np
import matplotlib.pyplot as p

#Condiciones iniciales

L = 1 #Longitud de la barra en metros 
total = 6000
n = 200 #Terminos de la serie
K = 237 #Coductividad termica del aluminio
C = 900 #Capacidad calorifica del aluminio
rho = 2700 #Densidad del aluminio

#Calculamos c
c = K/(C*rho) #Condición de estailidad de von Neumann-Courant

#Definimos las dimensiones de la malla para la gráfica
x = np.linspace(0,L, 100) #Usamos num = 100 para tener una buena gráfica
t = np.linspace(0,total, 100)

#Creación de la malla
X, tn = np.meshgrid(x, t)

#Realizamos la suma de los terminos de la serie de Fourier

T = np.zeros_like(X) #Array de ceros que será llenado con los terminos de la suma

# Serie de Fourier (solo términos impares)
for m in range(1, n + 1, 2):
    T += (400 / (m * np.pi)) * np.sin(m * np.pi * X / L) * np.exp(-c * (m * np.pi / L) ** 2 * tn)


#Grafica
fig = p.figure()
ax = fig.add_subplot(111, projection='3d')  #Una sola figura, una sola columna, primer subplot

ax.set_ylabel("Distancia (m)")
ax.set_xlabel("Tiempo (s)")
ax.set_zlabel("Temperatura (°C)")
ax.set_title('Temperatura en madera (serie de Fourier)')

sup = ax.plot_surface(tn,X,T, cmap='hot')

ax.set_xlim(0, 6001)
ax.set_ylim(-0.5, 1.3)
ax.set_zlim(0, 130)
fig.colorbar(sup)
p.show()


