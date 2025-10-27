# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 22:30:52 2025

@author: Susana A.S.R
"""

#Inciso a. Calcular seno con la serie finita con una Tolerancia de error 10-8
#No usar factoriales = Usar acumuladores

import math as m

from tabulate import tabulate

#Implementación de la función seno
def apsin(x,N):
    p = x #potencia
    f = 1.0 #factorial
    s = 1.0 #signo
    c = (s*p)/f #Valor incial de la suma
    for n in range(1,N):
        p *= x*x #Este es x**2
        f *= (2.0*n) * (2.0*n + 1.0)  #Este es para obtener el factorial
        s *= -1.0 #Este es (-1)**n
        c += (s*p) / f #está en radianes, convertir a grados
    return(c)

#Inciso C) Poner la tolerancia menor al epsilon de maquina 

def epsilon():
    e = 1.0
    t = 1.0
    while (1+e) != 1.0:
        t = e
        e = e/2
    return(t)

#Encontrar el n para el cual la tolerancia sea menor a 10^-8 (inciso a)
def Ntol(x):
    n = 1 #Comenzamos con un n inicial 
    while True:
        n += 1 #Sumamos un n cada que el if no se cumple,i.e, cuando el error absoluto aun es menor a la tolerancia
        if abs(apsin(x,n) - m.sin(x)) <= (epsilon()): #Esta condicion fue cambiada para poder ejercutar el inciso c
            break 
    return(n)

#Inciso B)
#Necesito reducir angulos grandes a angulos en el intervalo [0,360]
#Para eso voy a definir una función en donde ingrese grados_rad y me devuelva esa variable
#pero ahora con el angulo dentro de ese intervalo
 
def red(x,n):
    grado = x%360.0  #Obtiene el ángulo en el intervalo
    resul = apsin(grado, n) #Llama a la función para obtener la suma ya con el ángulo equivalente
    return resul


#Bucle para validar la entrada de datos
while True:
    grados = float(input("Ingrese el valor de x en grados: "))

    #Validamos que el usuario no haya ingresado un string
    try:
        grade = float(grados)
        
    except:
        print("Por favor ingrese números validos")
        continue
    break

#Convertir los grados ingresados en radianes
grados_rad = grados * (m.pi/180.0)

#LLamar la función de la suma
y = red(grados_rad, Ntol(grados_rad))


#Presentando resultados en una tabla
#Tabla
a = [
    [Ntol(grados_rad), y , abs((y - m.sin(grados_rad))/m.sin(grados_rad))] 
]

# N = está ajustado a la tolerancia del inciso C
headers = ["N","suma", "|(Suma - Sin(x))/ Sin(x)|"]

print(tabulate(a, headers=headers, tablefmt="grid"))

print("Resultado del mismo ángulo evaluado con la función seno(x) de python: ", m.sin(grados_rad))
 
    
    
    

