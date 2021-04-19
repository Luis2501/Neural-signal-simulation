#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Simulación de señales neuronales mediante circuitos RC (Clase 'Axon')

7º Concurso Estatal de Aparatos y Experimentos de Física
Luis Eduardo Sánchez González

lun 12 abr 2021 19:23:12 CDT 

Repositorio Github: https://github.com/Luis2501/Neural-signal-simulation
"""
import numpy as np

class Axon:
    
	def __init__(self, V0, C, R1, R2, N):

		"""
        	Constructor de la clase.

		------------------------
		Parámetros
		------------------------

		C: Capacitancia de la membrana
		R1: Resistencia de la membrana
		R2: Resistencia del axón 
		N: Número de circuitos
		"""

		self.C, self.R1, self.R2 = C, R1, R2  
		self.N = N        
		
		self.InitCond = np.zeros(N)
        
		if isinstance(V0, (int, float)):
        
			self.V0 = lambda t: V0  
			self.InitCond[0] = self.V0(0)
            
		elif callable(V0):
            
			self.V0 = V0 
			self.InitCond[0] = self.V0(0)
            
		else:
            
			raise ValueError("Voltaje no definido")
    
	def dV(self, Vi, Vf):

		"""	
		Ecuación diferencial.

		V' = 1/C [(V0 - V)/R2 - V/R1]   
		"""

		return (1/self.C)*(((Vi-Vf)/self.R2)-(Vf/self.R1))

	def __call__(self, v, t):
        
		V = np.zeros_like(v)
		V[0] = self.dV(self.V0(t), v[0])

		for i in range(len(v) - 1):
            
			V[i + 1] += self.dV(v[i], v[i + 1]) 

		return V
