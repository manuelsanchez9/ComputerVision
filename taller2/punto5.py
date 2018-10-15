# -*- coding: utf-8 -*-
"""
Created on Sat Oct 06 22:19:11 2018

@author: Manuel Andres Sanchez Muñoz

A. Seleccione una imagen en color. Lee tu imagen en Python. Luego, agregue 
ruido a la imagen en color. (np.random.uniform (0,75))

B. Filtra la imagen de color usando filtros gaussianos y medios. El tamaño del 
filtro debe ser 3x3, 5x5 y 7x7, y el sigma para el filtro gaussiano debe ser 
0.5, 0.7 y 1. Recuerde, filtrar una imagen en color requiere Para filtrar cada 
canal R-G-B.

C. Compara el resultado usando el MSE. Tenga en cuenta que necesita definir una
nueva función de MSE que compare Imágenes en color. En el informe, se incluye
el MSE para cada configuración y se presenta una discusión sobre cual es la 
mejor configuración para la imagen.
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters
import funciones as fun

Im = Image.open('fruitRGB.jpg').convert('RGB')
Im_a = np.array(Im)
plt.imshow(Im_a)
plt.title("Imagen Original")

[row, col, nb] = Im_a.shape
Im_n = np.zeros(Im_a.shape)
Im_n = Im_a+75*np.random.rand(row,col,nb)
Im_n = np.uint8(255*Im_n/Im_n.max())
plt.figure()
plt.imshow(Im_n)
plt.title("Imagen con ruido (0,75)")

Im_f1 = filters.uniform_filter(Im_n,3)
plt.figure()
plt.imshow(Im_f1)
mse_f1 = fun.my_mseRGB(Im_a,Im_f1)
plt.title("Imagen con filtro 3 x 3")
print ("MSE para uniforme 3 x 3 con ruido (0,75): " + str(mse_f1))

Im_f1 = filters.uniform_filter(Im_n,5)
plt.figure()
plt.imshow(Im_f1)
mse_f1 = fun.my_mseRGB(Im_a,Im_f1)
plt.title("Imagen con filtro 5 x 5")
print ("MSE para uniforme 5 x 5 con ruido (0,75): " + str(mse_f1))

Im_f1 = filters.uniform_filter(Im_n,7)
plt.figure()
plt.imshow(Im_f1)
mse_f1 = fun.my_mseRGB(Im_a,Im_f1)
plt.title("Imagen con filtro 7 x 7")
print ("MSE para uniforme 7 x 7 con ruido (0,75): " + str(mse_f1))
  
Im_f2 = filters.gaussian_filter(Im_n,0.5)
plt.figure()
plt.imshow(Im_f2)
mse_f2 = fun.my_mseRGB(Im_a,Im_f2)
plt.title("Imagen con filtro 0.5")
print ("MSE para gaussiano 0.5 con ruido (0,75): " + str(mse_f1))

Im_f2 = filters.gaussian_filter(Im_n,0.7)
plt.figure()
plt.imshow(Im_f2)
mse_f2 = fun.my_mseRGB(Im_a,Im_f2)
plt.title("Imagen con filtro 0.7")
print ("MSE para gaussiano 0.7 con ruido (0,75): " + str(mse_f1))

Im_f2 = filters.gaussian_filter(Im_n,1)
plt.figure()
plt.imshow(Im_f2)
mse_f2 = fun.my_mseRGB(Im_a,Im_f2)
plt.title("Imagen con filtro 1")
print ("MSE para gaussiano 1 con ruido (0,75): " + str(mse_f1))




