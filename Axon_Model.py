#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Simulación de señales neuronales mediante circuitos RC 

7º Concurso Estatal de Aparatos y Experimentos de Física
Luis Eduardo Sánchez González

lun 12 abr 2021 19:23:12 CDT 

Repositorio Github: https://github.com/Luis2501/Neural-signal-simulation
"""
import numpy as np

class Axon:
    
	def __init__(self, V0, C, R1, R2, N):
        
		self.C, self.R1, self.R2 = C, R1, R2  
        
		try:
        
			self.InitCond = np.zeros(N)
        
			if isinstance(V0, (int, float)):
        
				self.V0 = lambda t: V0  
            
			elif callable(V0):
            
				self.V0 = V0 
                
			self.InitCond[0] = self.V0(0)
            
		except:
            
			print("Voltaje no definido")
    
	def dV(self, Vi, Vf):
        
		return (1/self.C)*(((Vi-Vf)/self.R2) - (Vf/self.R1))

	def __call__(self, v, t):
        
		V = np.zeros_like(v)
		V[0] = self.dV(self.V0(t), v[0])

		for i in range(len(v) - 1):
            
			V[i + 1] += self.dV(v[i], v[i + 1]) 

		return V

if __name__ == "__main__":

	from sys import path
	path.append("../")
	import matplotlib.pyplot as plt
	from PhysicsPy.ODEsMethods import *

	Axon_0 = Axon(70e-3, 1e-10, 1e8, 1e6, N = 100)

	Solucion = Euler(Axon_0)
	Solucion.InitialConditions(Axon_0.InitCond, [0, 1e-2], 1e-6)
	V, t = Solucion.SolveODE()

	for i in range(0, len(t), 1000):

    		plt.plot(V[i,:], label ="t ="+f"{round(i*1e-6,3)} s")

	plt.title("Voltaje através de los circuitos")
	plt.grid() ; plt.legend() 
	plt.ylabel("Voltaje (V)")
	plt.xlabel("Circuito (N)")
	plt.show()
