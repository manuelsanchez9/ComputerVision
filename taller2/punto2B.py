# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:49:08 2018

@author: Manuel Andres Sanchez Muñoz

Punto 2

B. Mejore la imagen moon.jpg con el filtro Laplaciano usando de 4 vecinos 
y 8 vecinos, incluya en el informe las imágenes y analiza las diferencias 
en los resultados.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters

Im_g = Image.open('moon.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.figure()
plt.gray()
plt.imshow(Im_ga) 
plt.title("Imagen en escala de grises")

#[row, col] = Im_ga.shape;
#Im_n = np.double(Im_ga)

Im_laplaciano = filters.laplace(Im_ga)
plt.figure()
plt.gray()
plt.imshow(Im_laplaciano) 
plt.title("Filtro Laplaciano")