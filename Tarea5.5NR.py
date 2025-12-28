# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 12:30:52 2025

@author: Susana A.S.R

Tarea 5. Ejercicio 5
"""
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt

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

#Valor inicial de T
T = 3.0
dT=3.e-4   
Nmax=100;  #Pasos

# Definimos la función para obtener la energía
def I(N, T):
    return (2.0 * h * N ** 3.0 / c ** 2.0) * (1.0 / (n.exp(h * N / (kB * T)) - 1.0))

#creamos una la fución que minimiza chi^2
def chi2(I, nu, sigma, kB, h, c, T):
    # I(nu,T) modelo de Planck
    expo = n.exp(h * nu / (kB * T))
    planck = (2.0*h*nu**3.0 / c**2.0) / (expo - 1.0)

    # Derivada de I respecto a T
    planck_dT = (2.0*h*nu**3.0 / c**2.0) * (h*nu/(kB*T**2.0)) * (expo / (expo - 1.0)**2.0)

    # Derivada total de chi^2 respecto T
    return n.sum( 2.0 * (I - planck) * planck_dT / sigma**2.0 )

#Método de Newton-Raphson unidimesional 
def NewtonR(T,dT,sigma,Nmax):
    #Tolerancia para el método
    tol = 1e-6
    for i in range(Nmax):
        F =  chi2(I_e, Nu, sigma, kB, h, c, T)
        
        # derivada numérica central
        F_mas = chi2(I_e, Nu, sigma, kB, h, c, T + dT/2.0) #Evaluamos chi2 un paso arriba
        F_menos = chi2(I_e, Nu, sigma, kB, h, c, T - dT/2.0) #Evaluamos chi2 un paso abajo
        df = (F_mas - F_menos)/dT #Diferencia
        dT=-F/df 
        T+=dT  
        
        # Criterio de paro REAL
        if abs(dT) <= tol:
            print(f"T_estimada = {T:.6f} K")
            print(f"Error = {abs(dT):.3e} K")
            return T
    return T

T_estimada = NewtonR(T,dT,Incertidumbre,Nmax)

#Gráficar
#Regresamos a la unidades presentadas en los datos originales
nu_plot = n.linspace(Nu.min() * 0.95, Nu.max() * 1.05, 2000)  # En Hz

# Calcular el modelo usando la función I (ya está en W/m²/Hz/sr)
model_plot = I(nu_plot, T_estimada)/ 1e-20  # Pasamos de W/m²/Hz/sr a MJy/sr
plt.figure(figsize=(8, 5))

# Datos 
plt.errorbar(nu, I_e/1e-20, yerr=Incertidumbre/1000.0, fmt='o', ms=4, 
             label='Datos experimentales', color='blue', ecolor='black', capsize=3)
# Modelo ajustado
plt.plot(nu_plot/cs, model_plot, 'r-', label=f'Datos COBE y Ajuste de Cuerpo Negro(T={T_estimada:.4f} K)')
plt.xlabel(r"$\tilde\nu$ (1/cm)")
plt.ylabel("Intensidad (MJy/sr)")
plt.title("Datos COBE con ajuste de cuerpo negro")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

