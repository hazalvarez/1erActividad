# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 12:25:06 2022

@author: ico
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace

P = np.array([[2, 3], [5, 4], [7, -3], [2, 3]], dtype = float)
h = -3
k = 4
figure, ax = plt.subplots()
ax.plot(P[:, 0], P[:, 1])
ax.plot(P[:, 0] + h, P[:, 1] + k)
ax.grid()
ax.set_title("Translacion")
plt.show()