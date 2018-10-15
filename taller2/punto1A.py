# -*- coding: utf-8 -*-
"""
Created on Sat Oct 06 16:37:50 2018

@author: Manuel Andres Sanchez Muñoz

Continuacion punto 1
"""

import numpy as np
from PIL import Image
from scipy.ndimage import filters
import funciones as fun
import matplotlib.pyplot as plt

Im_g = Image.open('coins.jpg').convert('L')
Im_ga = np.array(Im_g)

umbral=160

[row, col] = Im_ga.shape;
Im_n80 = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n80[i,j] = Im_n80[i,j]+np.random.uniform(0,80)
        
Im_h80 = np.uint8(Im_n80)

if_unif = filters.uniform_filter(Im_n80,3)

if_gaus = filters.gaussian_filter(Im_n80,0.7)

Im_ga_bn = fun.my_threshold(Im_ga, umbral)
plt.figure()
plt.gray()
plt.imshow(Im_ga_bn)
plt.title("Imagen original blanco y negro")

Im_h80_bn = fun.my_threshold(Im_h80, umbral)
plt.figure()
plt.gray()
plt.imshow(Im_h80_bn)
plt.title("Imagen blanco y negro con ruido (0.80)")

Im_unif_bn = fun.my_threshold(if_unif, umbral)
plt.figure()
plt.gray()
plt.imshow(Im_unif_bn)
plt.title("Imagen blanco y negro del filtro uniforme")

Im_ga_bn = fun.my_threshold(if_gaus, umbral)
plt.figure()
plt.gray()
plt.imshow(Im_ga_bn)
plt.title("Imagen blanco y negro del filtro Gaussiano")







