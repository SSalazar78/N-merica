# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 16:28:52 2025

@author: Susana A.S.R

Tarea 6.2

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leyendo los datos del archivo Jpsimumu_Run2011A.csv
data = pd.read_csv('MuRun2010B.csv')

#Asigando los datos necesarios
#1
E1 = data.iloc[:,3].values
px1 = data.iloc[:,4].values
py1 = data.iloc[:,5].values
pz1 = data.iloc[:,6].values

#2
E2 = data.iloc[:,12].values
px2 = data.iloc[:,13].values
py2 = data.iloc[:,14].values
pz2 = data.iloc[:,15].values

#Calculo del momento y energía total al cuadrado
Et = (E1 + E2)**2
P = (px1 + px2)**2 + (py1 + py2)**2 + (pz1 + pz2)**2 

#Calculo de la masa (relación invariante)
m = np.sqrt(Et - P)

#Elaboración del historigrama
plt.figure()

#Encontar la masa promedio en el historigrama
m_prom = np.mean(m) #Aquí se obtiene la masa que podría ser de la partícula Y(ns)

plt.axvline(92, color = 'green', linestyle = '--', linewidth=0.9)
plt.legend()
plt.hist(m,bins = 120, rwidth=0.5 )
plt.xlabel('Masa (GeV)') #Omitimos c^2 en el denominador pues C=1
plt.ylabel('Número de eventos')
plt.semilogy()
plt.title('Historigrama de la masa de la partícula que decae')

