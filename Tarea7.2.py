# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 14:11:24 2025

@author: Susana A.S.R
"""
import numpy as np

#Números aleatorios
x = np.random.random(1000)

#Ordenamos los números generados 
xn = np.sort(x)

#Calculo de la distribución teorica
"""Como queremos determinar si los números generados cumplen
una distribución uniforme, F(x) = x"""
Fx = xn

#Calculo de la distribución empírica
"""Según la formula (13), podemos considerar la distribución empírica 
para Kn+ como j/n y para Kn- como j-1/n"""

n = len(xn) #Tamaño

Fn_mas = np.arange(1, n+1)/n 

Fn_menos = np.arange(0, n)/n

#Calculo de Kn+ y Kn-

Kn_mas = np.sqrt(n) * np.max(Fn_mas - Fx)

Kn_menos = np.sqrt(n) * np.max(Fx - Fn_menos)

"""Confiabilidad que queremos para el test p = 95% entonces yp = 1.2239, 
con estos parametros haremos la comparación de los Kn+ y Kn- """

p = 95 #Porcentaje 
yp = 1.2239 #Valor correspondiente según la tabla 2

#Calculo del valor crítico con la formula para n>30
Valor_c = yp - 1/(6 * np.sqrt(n))

#Si rechazar = False si hay una distribución uniforme
#Si rechazar = True no hay distribución uniforme
rechazar = (Kn_mas > Valor_c) or (Kn_menos > Valor_c)

if rechazar == False:
    print('Los números generados si cumplen con una distribución uniforme')
    
if rechazar == True:
    print('Los números generados no cumplen con una distribución uniforme')


