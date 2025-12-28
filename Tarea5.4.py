# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 13:42:46 2025

@author: Susana A.S.R

Tarea 5. Ejercicio 4
"""
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt

#Importamos los datos
data = pd.read_csv('RLC.txt', header=0, delim_whitespace=True)

#Declaramos los arreglos
T = data.iloc[:, 0].values #Tiempo (ns), x
Volt = data.iloc[:,1].values #Voltaje (V), y
sigma = data.iloc[:,2].values # V

# Linealización 
y = n.log(Volt)
sigma_y = sigma/ Volt 
w = 1.0 / sigma_y**2 #Función peso 

# Sumas para minimos cuadrados 
S = n.sum(w)
Sx = n.sum(w * T)
Sy = n.sum(w * y)
Sxx = n.sum(w * (T)**2)
Sxy = n.sum(w * T * y)

# Calculamos los parametros de ajuste
Delta = (S * Sxx) - (Sx)**2

# a = In(V0)
a = (Sxx*Sy - Sx*Sxy)/Delta

# b = -Gamma
b = (S*Sxy - Sx*Sy)/Delta

# Calculo de incertidumbres para a y b
sigma_a = n.sqrt(Sxx/Delta)
sigma_b = n.sqrt(S/Delta)

# Obteniendo V0 y Gamma ajustados con sus incertidumbres
V0 = n.exp(a)
Gamma = -b
sigmaV0 = V0*sigma_a 
sigma_g = sigma_b

#Imprimimos los resultados
print('Resultados del ajuste:')
print(f'V0 = {V0:.6f} ± {sigmaV0:.6f} V')
print(f'Γ = {Gamma:.6f} ± {sigma_g:.6f} ns⁻¹')

# Inciso B) Determinar Chi^2
y_mod = a + b * T #Ec. recta
chi2 = n.sum(w * (y - y_mod)**2)
print(f'χ² = {chi2:.4f}')

# Reduciendo Chi^2
N = len(T) #Número de datos

# Inciso C) Gráfica semi-log
t = n.arange(0, 500, 0.1) #Puntos a gráficar

# Curva de ajuste
V_fit = V0 * n.exp(-Gamma * t)  # Modelo exponencial con parámetros ajustados

# Graficar
plt.figure(figsize=(10, 6))

# Datos experimentales con errores
plt.errorbar(T, Volt, yerr=sigma, fmt='o', color='blue', elinewidth=1, capsize=4, capthick=1, alpha=0.7,label='Datos experimentales')
# Curva de ajuste
plt.plot(t, V_fit, 'r-', linewidth=2, label=f'Ajuste: $V(t) = {V0:.3f}e^{{-{Gamma:.3f}t}}$')
plt.xlabel(r'Tiempo [ns]')
plt.ylabel(r'V(t) [V]')
plt.yscale("log")
plt.title('Ajuste por mínimos cuadrados del circuito RL', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3, which='both')  # 'both' para grid en escala logarítmica
plt.show()