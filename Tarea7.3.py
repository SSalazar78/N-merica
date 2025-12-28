# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 20:19:51 2025

@author: Susana A.S.R

Ejercicio 3.A
"""
import numpy as np

#Constantes
masa = 139.6 #Masa de los piones en MeV/c
K = 200 #Energía cinetica dada en MeV/c
tao = 2.6e-8 #Tiempo de vida promedio de los piones en el sistema en reposo
c = 3e8 #Velocidad de la luz
d = 20 #Distancia a viajar en metros
N0 = int(1e6) #Tamaño inicial de la muestra de piones

#Calculo de la Energía total
Et = K + masa

#Factor de Lorentz (efecto relativista)
gamma = 1.0 + (K/masa)
tao_lab = tao*gamma #Tiempo de vida del pion visto del sistema laboratorio

#Calculo de la velocidad
v = c * np.sqrt(1.0 - (1.0/(gamma)**2.0))

#Tiempo en el que recorre d
t = d/v #Usamos la forma clásica. Sistema Laboratorio

#Pasamos a la simulación montecarlo
#Generar tiempos de decaimiento exponenciales
R = np.random.rand(N0)
t_d = -tao_lab * np.log(1-R) #Tiempos aleatorios de decaimiento

#Condición: sobrevive si NO decae antes de llegar
N = np.sum(t_d > t)


print("Número de piones que sobreviven los 20 metros:", N)
print("Fracción de supervivencia:", N/N0)

