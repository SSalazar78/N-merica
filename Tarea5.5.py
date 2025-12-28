# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 21:56:08 2025

@author: Susana A.S.R

Tarea 5. Ejercicio 5
"""
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit #Utiliza mínimos cuadrados no lineales para ajustar una función, f, a los datos.

# Constantes
h = 6.62607015e-34  # Constante de Planck J/s
c = 3e8  # Velocidad de la luz en m/s
cs = 3e10  # Velocidad de la luz en cm/s
kB = 1.380649e-23  # Constante de Boltzmann J/K

# Lectura del archivo .txt para obtener los datos
data = pd.read_csv('COBE.txt', header=0, delim_whitespace=True)

# Asignando los datos
nu = data.iloc[:, 0].values  # Número de onda cm^-1

I_e = 1e-20*data.iloc[:, 1].values # Intensidad MJy/sr (Mega-Jansky por sr) convertidos a W/m^2*Hz*sr

Incertidumbre = 1e-23*data.iloc[:, 2]. values # Sigma kJy/sr (kilo-Jansky por sr) convertidos a W/m^2*Hz*sr

#Convertimos a frecuencia (1/s)
Nu = nu*cs 

# Inciso A) Gráfica de los datos con la incertidumbre
# COMPONER MÁS DE UNA LABEL
plt.errorbar(Nu, I_e, yerr=Incertidumbre, fmt='.', color='blue',
             ecolor='black', elinewidth=1, capsize=4, label=('Datos'))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Intensidad (W/m²/Hz/sr)")
plt.title("Datos COBE (SI)")
plt.grid(True)
plt.legend()
plt.show()

# Inciso B)

#Número de terminos para la suma 
N = len(Nu)

# Definimos la función para obtener la energía
def I(N, T):
    return (2 * h * N ** 3 / c ** 2) * (1 / (n.exp(h * N / (kB * T)) - 1))

#Ajuste por minimos cuadrados no lienales
Ti = 1.0  #Valor aleatorio para iniciar el ajuste

#Curve_fit regresa el valor ajustado para T y su Incertidumbre
popt, pcov = curve_fit(I, Nu, I_e, p0=[Ti], sigma=Incertidumbre,
                       absolute_sigma=True, maxfev=200000)

T_A = popt[0] #Valor ajustado de T
T_I = n.sqrt(n.abs(pcov[0,0])) #Incertidumbre estadística de la temperatura
T_T = 2.725 #Valor teorico 
print(f"T ajustada (covariancia) = {T_A:.6f} K ± {T_I:.6e} K")
print(f"T teorico = {T_A:.6f} K")

# ---------------------------
# GRÁFICOS: datos vs ajuste  ARREGLAR 
# ---------------------------
# Usar Hz en el eje x y W/m²/Hz/sr en el eje y
nu_plot = n.linspace(Nu.min() * 0.95, Nu.max() * 1.05, 2000)  # En Hz

# Calcular el modelo usando la función I (ya está en W/m²/Hz/sr)
model_plot = I(nu_plot, T_A)/ 1e-20  # Pasamos de W/m²/Hz/sr a MJy/sr

plt.figure(figsize=(8, 5))

# Datos 
plt.errorbar(nu, I_e/1e-20, yerr=Incertidumbre/1000.0, fmt='o', ms=4, 
             label='Datos', color='blue', ecolor='black', capsize=3)
# Modelo ajustado
plt.plot(nu_plot/cs, model_plot, 'r-', label=f'Planck (T={T_A:.3f} K)')
plt.xlabel(r"$\tilde\nu$ (1/cm)")
plt.ylabel("Intensidad (MJy/sr)")
plt.title("Datos COBE con ajuste de cuerpo negro")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

