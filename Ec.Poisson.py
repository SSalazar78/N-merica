# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:14:44 2025

@author: Susana A.S.R
"""

#Importamos librerias
import numpy as n
import matplotlib.pyplot as p

#Definiciones
N = 100 #Tamaño de la malla
L = 2*n.pi #
tol = 1e-7 #Criterio de convergencia


#Pasos (ambos serán igualmente espaciados)
dx = L/(N - 1)
dy = dx

#Creación de la malla y la distribución de carga
m = n.zeros((N,N)) 


#Función f(x,y)
def f(x,y):
    return(n.cos(3*x + 4*y) - n.cos(5*x - 2*y))

#Hacemos una función en donde se llevará a cabo el método de Gauss-Seidel

for k in range(5000):
    
    error = 0.0
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            m_ant = m[i,j] #Guardamos el valor anterior de m[i,j] antes de calcular el siguiente
            
            m[i,j] = (0.25) * (m[i+1,j] + m[i-1,j] + m[i,j+1] + m[i,j-1] - dx**2 * f(i*dx, j*dy) ) 
            
            diff = abs(m[i,j] - m_ant)
            if diff > error:
                error = diff
    #Condiciones de frontera impuestas en el problema
    m[0, :]  = m[N-2, :]    # fila superior igual a la penúltima
    m[N-1, :] = m[1, :]     # fila inferior igual a la segunda
    m[:, 0]  = m[:, N-2]    # columna izquierda igual a la penúltima
    m[:, N-1] = m[:, 1]     # columna derecha igual a la segunda
    
    if error < tol:
        break #La convergencia se alcanza en una de las iteraciones

# Crear la malla para graficar
x = n.linspace(0, L, N)
y = n.linspace(0, L, N)
X, Y = n.meshgrid(x, y)

# Graficar la solución
fig = p.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, m, cmap='magma')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Solución de la ecuación de Poisson mediante Gauss-Seidel')
p.colorbar(surf)
p.show()
