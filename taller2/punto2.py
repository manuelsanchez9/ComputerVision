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
import funciones as fun

Im_g = Image.open('build.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga) 
plt.title("Imagen Original")    

[Ig, Ix, Iy] = fun.my_gradient(Im_ga)
plt.figure()
plt.gray()
plt.imshow(Ig) 
plt.title("Gradiente")    

Im_g = Image.open('moon.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.figure()
plt.gray()
plt.imshow(Im_ga) 
plt.title("Imagen en escala de grises")

Imla4vec = fun.my_laplace_4_vecinos(Im_ga)
Im_lap_mos4vec = np.uint8(Imla4vec)
plt.figure()
plt.gray()
plt.imshow(Im_lap_mos4vec) 
plt.title("Filtro Laplaciano con 4 vecinos")

Imla8vec = fun.my_laplace_8_vecinos(Im_ga)
Im_lap_mos8vec = np.uint8(Imla8vec) 
plt.figure()
plt.gray()
plt.imshow(Im_lap_mos8vec) 
plt.title("Filtro Laplaciano con 8 vecinos")







