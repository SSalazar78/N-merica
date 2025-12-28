# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 15:15:05 2025

@author: Susana A.S.R

Tarea 6.1

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from tabulate import tabulate

# Calculo de la incertidumbre mediante incertidumbre estandar
def incertidumbre(masas, masa_pico, ventana):
    # Seleccionar las masas alrededor de la masa pico 
    filtro = np.abs(masas - masa_pico) < ventana #Distancia entre las masas
    q_j = masas[filtro] #En los qj se guardan las masas que cumplen con el filtro 
    n = len(q_j) #Cantidad de masas 
    
    # Desviación estándar 
    s_q = np.std(q_j)
    
    # Incertidumbre estándar  
    u = s_q / np.sqrt(n)
    
    return u

#Leyendo los datos del archivo Jpsimumu_Run2011A.csv
data = pd.read_csv('Jpsimumu_Run2011A.csv')

#Asigando los datos necesarios
#Dimoun 1
E1 = data.iloc[:,3].values
px1 = data.iloc[:,4].values
py1 = data.iloc[:,5].values
pz1 = data.iloc[:,6].values

#Dimuon 2
E2 = data.iloc[:,12].values
px2 = data.iloc[:,13].values
py2 = data.iloc[:,14].values
pz2 = data.iloc[:,15].values

#Calculo del momento y energía total al cuadrado
Et = (E1 + E2)**2
P = (px1 + px2)**2 + (py1 + py2)**2 + (pz1 + pz2)**2 

#Calculo de la masa (relación invariante)
m = np.sqrt(Et - P)

# Elaboración del histograma
plt.figure()

# Obtener histograma sin graficarlo para encontrar los picos
counts, bin_edges = np.histogram(m, bins=150)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

# Encontrar los picos 
peaks, properties = find_peaks(counts, height=200, distance=10)

# Calcular las masas en los centros de los bins donde hay picos
masas = []
peak_heights = []

for peak in peaks:
    masa_valor = 0.5 * (bin_edges[peak] + bin_edges[peak + 1])# Masa en el centro del bin del pico
    alt_valor = counts[peak] #Altura del pico
    
    #Añadimos lo anterior a los arreglos 
    masas.append(masa_valor) 
    peak_heights.append(alt_valor)

# Crear tabla con los resultados
table_data = []
for i, (masa, altura) in enumerate(zip(masas, peak_heights)):
    table_data.append([f"Pico {i+1}", f"{masa:.3f}", f"{altura:.0f}"])

# Mostrar tabla de todos los picos detectados
print("Masas y alturas de los picos detectados en el historigrama")
print(tabulate(table_data, headers=["Pico", "Masa (GeV)", "Altura"], tablefmt="grid"))

# Ordena los picos por altura 
picos_ordenados = peaks[np.argsort(counts[peaks])[::-1]]

#Selecciono los picos que si tienen significado
pico1 = picos_ordenados[0]   #correspondiente a J/psi(1S)
pico2 = picos_ordenados[3]   #correspondiente a psi(2S)

# Masas de los picos 
m_1 = 0.5 * (bin_edges[pico1] + bin_edges[pico1 + 1])
m_2 = 0.5 * (bin_edges[pico2] + bin_edges[pico2 + 1])

# Calcular incertidumbre para J/psi(1S)
error1 = incertidumbre(m, m_1, ventana=0.05)

# Calcular incertidumbre para psi(2S)
error2 = incertidumbre(m, m_2, ventana=0.05)

# Resultados
print("Resultados:")
print(f"J/ψ(1S) = {m_1:.3f} ± {error1:.4f} GeV")
print(f"ψ(2S)  = {m_2:.3f} ± {error2:.4f} GeV")

# Graficar el histograma 
plt.hist(m, bins=150, rwidth=0.5, alpha=0.7, color='blue', label='Datos')
# Marcar los picos con sus incertidumbres
plt.axvline(m_1, color='red', linestyle='--', linewidth=0.9, label=f'J/ψ(1S) = {m_1:.3f} ± {error1:.4f} GeV')
plt.axvline(m_2, color='green', linestyle='--', linewidth=0.9, label=f'ψ(2S) = {m_2:.3f} ± {error2:.4f} GeV')
plt.xlabel('Masa (GeV)')
plt.ylabel('Frecuencia')
plt.title('Histograma de la masa de la partícula que decae')
plt.grid()
plt.legend()
plt.show()


