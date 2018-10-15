# -*- coding: utf-8 -*-
"""
Created on Mon Oct 08 10:20:29 2018

@author: Manuel Sanchez
"""
import numpy as np
from PIL import Image
from scipy.ndimage import filters
import funciones as fun
import matplotlib.pyplot as plt

# Umbral para funcion my_threshold
umbral=160

# Cargar una imagen y pasarla a escala de grises
Im_g = Image.open('coins.jpg').convert('L')
Im_ga = np.array(Im_g)

# Imprimir la imagen original
plt.figure()
plt.gray()
plt.imshow(Im_ga)
plt.title("Imagen original")

# Agregar ruido (0,60) a una imagen en escala de grises
[row, col] = Im_ga.shape;
Im_n60 = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n60[i,j] = Im_n60[i,j]+np.random.uniform(0,60)

# Imprimir imagen con ruido (0,60) en escala de grises
plt.figure()
plt.gray()
plt.imshow(Im_n60)
plt.title("Imagen con ruido (0,60)")

# MSE entre imagen original e imagen con filtro uniforme de 3 x 3 en escala de grises
Im_f1u = filters.uniform_filter(Im_n60,3)
print ("MSE para uniforme 3 x 3 con ruido (0,60): " + str(fun.my_mse(Im_f1u, Im_g)))

# MSE entre imagen original e imagen con filtro Gaussiano de 0.5 en escala de grises
Im_f1g = filters.gaussian_filter(Im_n60,0.5)
print ("MSE para gaussiano 1 con ruido (0,60): " + str(fun.my_mse(Im_f1g, Im_g)))

# Imprimir imagen con filtro uniforme 3 x 3 en escala de grises
plt.figure()
plt.gray()
plt.imshow(Im_f1u)
plt.title("Imagen con filtro uniforme de 3 x 3")

# Imprimir imagen con filtro Gaussiano 0.5 en escala de grises
plt.figure()
plt.gray()
plt.imshow(Im_f1u)
plt.title("Imagen con filtro Gaussiano 0.5")

# Imprimir histograma imagen original
Im_h = np.uint8(Im_ga)
h = fun.my_hist(Im_h)
plt.figure()
plt.bar(np.arange(256),h)
plt.title("Histograma imagen original")

# Imprimir histograma imagen con ruido (0,60)
Im_h60 = np.uint8(Im_n60)
hruido = fun.my_hist(Im_h60)
plt.figure()
plt.bar(np.arange(256),hruido)
plt.title("Histograma con ruido (0,60)")

# Imprimir histograma imagen filtro uniforme 3 x 3
Im_h3x3 = np.uint8(Im_f1u)
h3x3 = fun.my_hist(Im_h3x3)
plt.figure()
plt.bar(np.arange(256),h3x3)
plt.title("Histograma imagen con filtro 3 x 3")

# Imprimir histograma imagen filtro Gaussiano 0,5
Im_05 = np.uint8(Im_f1g)
h_05 = fun.my_hist(Im_05)
plt.figure()
plt.bar(np.arange(256),h_05)
plt.title("Histograma imagen con filtro 0,5")

# Imprimir imagen desde my_threshold (Blanco y negro) 
Im_ga_bn = fun.my_threshold(Im_ga, umbral)
plt.figure()
plt.gray()
plt.imshow(Im_ga_bn)
plt.title("Imagen original blanco y negro")