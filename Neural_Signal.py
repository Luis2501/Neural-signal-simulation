#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Simulación de señales neuronales mediante circuitos RC (Voltaje constante en el tiempo)

7º Concurso Estatal de Aparatos y Experimentos de Física
Luis Eduardo Sánchez González

lun 12 abr 2021 19:23:12 CDT 

Repositorio Github: https://github.com/Luis2501/Neural-signal-simulation
"""
import numpy as np
from Axon_Model import Axon
import matplotlib.pyplot as plt
from PhysicsPy.ODEsMethods import *

axon = Axon(70e-3, 1e-10, 1e8, 1e6, N = 100)						

Solucion = Euler(axon)
Solucion.InitialConditions(axon.InitCond, [0, 1e-2], 1e-6)
V, t = Solucion.SolveODE()

for i in range(0, len(t), 1000):

	plt.plot(V[i,:], label ="t ="+f"{round(i*1e-6,3)} s")

plt.title("Voltaje através de los circuitos")
plt.grid() ; plt.legend() 
plt.ylabel("Voltaje (V)")
plt.xlabel("Circuito (N)")
plt.show()
