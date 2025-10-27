# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 22:24:57 2025

@author: Susana A.S.R
"""

#El epsilon de maquina cumple esta relación 1 + e != 1.
#Haré un while que se ejecute hasta que la condicion anterior no se cumpla
#es decir, hasta que e sea un cero para la maquina.

def epsilon():
    e = 1.0
    t = 1.0
    while (1+e) != 1.0:
        t = e
        e = e/2
    return(t)

print("El epsilon de maquina es: ",epsilon())

