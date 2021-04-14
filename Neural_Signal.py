#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Simulación de señales neuronales mediante circuitos RC (Voltaje variable en el tiempo)

7º Concurso Estatal de Aparatos y Experimentos de Física
Luis Eduardo Sánchez González

lun 12 abr 2021 19:23:12 CDT 

Repositorio Github: https://github.com/Luis2501/Neural-signal-simulation
"""
import numpy as np
from sys import path
path.append("../")
from Axon_Model import Axon
import matplotlib.pyplot as plt
from PhysicsPy.ODEsMethods import *

V0 = lambda t: 0.1*np.sin(2*np.pi*200*t)

Axon = Axon(V0, 1e-10, 1e8, 1e6, N = 100)

Solucion = Euler(Axon)
Solucion.InitialConditions(Axon.InitCond, [0, 0.05], 1e-6)
V, t = Solucion.SolveODE()

fig, (ax1,ax2) = plt.subplots(2, 1) 

#Gráfica señal de entrada
ax1.set_title("Señal de entrada")
ax1.plot(t, V0(t), color="blue", label="V(t)")  
ax1.set_xlabel(r"tiempo (s)")  
ax1.set_ylabel(r"Voltaje (V)") 
ax1.grid() ; ax1.legend() 
		
#Gráfica señal de salida
ax2.set_title("Señal de salida")
ax2.plot(t, V[:,-1], color="orange", label="V(t)")  
ax2.set_xlabel("tiempo (s)") 
ax2.set_ylabel("Voltaje (V)")
ax2.grid() ; ax2.legend() 

fig.tight_layout()
plt.show()
