# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:35:06 2022

@author: ico
"""

import numpy as np
import matplotlib.pyplot as plt

P = np.array([[2, 3], [5, 4], [7, -3], [2, 3]], dtype = float)
Rx = np.array([[1, 0], [0, -1]], dtype = float)
T = P@Rx  #Multiplicacion de matrices el arroba 
#definimos un objeto tipo figure
fig = plt.figure()
#ax yaxl son las sub graficas
ax = fig.add_subplot(1, 2, 1)
ax.plot(P[:, 0], P[:, 1])
ax.grid()
ax.set_title("Figura original")
axl = fig.add_subplot(1, 2, 2)
axl.plot(T[:, 0], T[:, 1])
axl.grid()
axl.set_title("Reflexion en el eje X")