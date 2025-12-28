# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 21:41:40 2025

@author: Susana A.S.R

Ejercicio 3.B
"""
import numpy as np

#Constantes
masa = 139.6 #Masa de los piones en MeV/c
E_p = 200 #Energía promedio en MeV/c
sigma = 50 #En MeV
tao = 2.6e-8 #Tiempo de vida promedio de los piones en el sistema en reposo
c = 3e8 #Velocidad de la luz
d = 20 #Distancia a viajar en metros
N0 = int(1e6) #Tamaño inicial de la muestra de piones


#Generar energías de piones con distribución gaussiana
Energias = np.random.normal(E_p, sigma, N0) #np.random.normal(Ubicación, Escala, Tamaño)

#Filtro para las energías generadas anteriormente que esten por debajo de la masa del pion
Energias = Energias[Energias > masa] #Selecciona solo las energías mayores a la masa  
 
#Factor de Lorentz (efecto relativista)
gamma = 1.0 + (Energias/masa)


#Tiempo de vida del pion visto del sistema laboratorio
tao_lab = tao*gamma 

#Calculo de la velocidad
v = c * np.sqrt(1.0 - (1.0/(gamma)**2.0))

#Tiempo en el que recorre d
t = d/v #Usamos la forma clásica
#print('Tiempo para recorrer 20m:',t)

#Pasamos a la simulación montecarlo
#Generar tiempos de decaimiento exponenciales
R = np.random.rand(len(tao_lab)) #Al filtrar las energías, ya no usamos N0 
t_d = -tao_lab * np.log(1-R) #Tiempos aleatorios de decaimiento

#Condición: sobrevive si NO decae antes de llegar
N = np.sum(t_d > t)


print("Número de piones que sobreviven los 20 metros:", N)
print("Fracción de supervivencia:", N/N0)



