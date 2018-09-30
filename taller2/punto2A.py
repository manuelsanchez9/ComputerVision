# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:17:12 2018

@author: Manuel Andres Sanchez Muñoz

Punto 2

A. En la imagen build.jpg, calcule las diferencias parciales usando filtros 
Sobel. Luego, calcule el gradiente y Laplaciano. Incluir en el informe:
    
(i) las imágenes
(ii) analizar las diferencias en los resultados.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters
import funciones as fun

Im_g = Image.open('build.jpg').convert('L')
Im_ga = np.array(Im_g)

Im_sobel = filters.sobel(Im_ga)
plt.figure()
plt.gray()
plt.imshow(Im_sobel) 
plt.title("Filtro Sobel")

[Ig, Ix, Iy] = fun.my_gradient(Im_sobel)
plt.figure()
plt.gray()
plt.imshow(Ig) 
plt.title("Gradiente")    

Im_laplaciano = filters.laplace(Im_ga)
plt.figure()
plt.gray()
plt.imshow(Im_laplaciano) 
plt.title("Filtro Laplaciano")






