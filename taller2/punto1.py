# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 07:03:55 2018

@author: Manuel Andres Sanchez Muñoz

Punto 1
"""

import numpy as np
from PIL import Image
from scipy.ndimage import filters
import funciones as fun
import matplotlib.pyplot as plt

Im_g = Image.open('coins.jpg').convert('L')
Im_ga = np.array(Im_g)

[row, col] = Im_ga.shape;
Im_n60 = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n60[i,j] = Im_n60[i,j]+np.random.uniform(0,60)


Im_f1u = filters.uniform_filter(Im_n60,3)
print ("MSE para uniforme 3 x 3 con ruido 0,60: " + str(fun.my_mse(Im_f1u, Im_g)))

Im_f1 = filters.uniform_filter(Im_n60,5)
print ("MSE para uniforme 5 x 5 con ruido 0,60: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n60,7)
print ("MSE para uniforme 7 x 7 con ruido 0,60: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n60,9)
print ("MSE para uniforme 9 x 9 con ruido 0,60: " + str(fun.my_mse(Im_f1, Im_g)))

[row, col] = Im_ga.shape;
Im_n80 = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n80[i,j] = Im_n80[i,j]+np.random.uniform(0,80)

Im_f1 = filters.uniform_filter(Im_n80,3)
print ("MSE para uniforme 3 x 3 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n80,5)
print ("MSE para uniforme 5 x 5 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n80,7)
print ("MSE para uniforme 7 x 7 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n80,9)
print ("MSE para uniforme 9 x 9 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

[row, col] = Im_ga.shape;
Im_n100 = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n100[i,j] = Im_n100[i,j]+np.random.uniform(0,100)

Im_f1 = filters.uniform_filter(Im_n100,3)
print ("MSE para uniforme 3 x 3 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n100,5)
print ("MSE para uniforme 5 x 5 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n100,7)
print ("MSE para uniforme 7 x 7 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.uniform_filter(Im_n100,9)
print ("MSE para uniforme 9 x 9 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

#Gaussiano

Im_f1g = filters.gaussian_filter(Im_n60,0.5)
print ("MSE para gaussiano 0.5 con ruido 0,60: " + str(fun.my_mse(Im_f1g, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n60,0.7)
print ("MSE para gaussiano 0.7 con ruido 0,60: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n60,1)
print ("MSE para gaussiano 1 con ruido 0,60: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n60,1.5)
print ("MSE para gaussiano 1.5 con ruido 0,60: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n80,0.5)
print ("MSE para gaussiano 0.5 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n80,0.7)
print ("MSE para gaussiano 0.7 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))
plt.figure()
plt.gray()
plt.imshow(Im_f1)
plt.title("Imagen filtro con 0,7")

Im_f1 = filters.gaussian_filter(Im_n80,1)
print ("MSE para gaussiano 1 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n80,1.5)
print ("MSE para gaussiano 1.5 con ruido 0,80: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n100,0.5)
print ("MSE para gaussiano 0.5 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n100,0.7)
print ("MSE para gaussiano 0.7 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n100,1)
print ("MSE para gaussiano 1 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_f1 = filters.gaussian_filter(Im_n100,1.5)
print ("MSE para gaussiano 1.5 con ruido 0,100: " + str(fun.my_mse(Im_f1, Im_g)))

Im_g = Image.open('coins.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.title("Imagen original en escala de grises")
horiginal = fun.my_hist(Im_ga)
plt.figure()
plt.bar(np.arange(256),horiginal)
plt.title("Histograma original")

[row, col] = Im_ga.shape;
Im_n80 = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n80[i,j] = Im_n80[i,j]+np.random.uniform(0,80)
        
plt.figure()
plt.gray()
plt.imshow(Im_n80)
Im_h80 = np.uint8(Im_n80)
plt.title("Imagen con ruido 0,80")
hruido = fun.my_hist(Im_h80)
plt.figure()
plt.bar(np.arange(256),hruido)
plt.title("Histograma con ruido (0,80)")

if_unif = filters.uniform_filter(Im_n80,3)
plt.figure()
plt.gray()
plt.imshow(if_unif)
plt.title("Imagen con filtro 3 x 3")

Im_3x3 = np.uint8(if_unif)
h3x3 = fun.my_hist(Im_3x3)
plt.figure()
plt.bar(np.arange(256),h3x3)
plt.title("Histograma imagen 3 x 3")

if_gaus = filters.gaussian_filter(Im_n80,0.7)
plt.figure()
plt.gray()
plt.imshow(if_gaus)
plt.title("Imagen con filtro 0.7")

Im_07 = np.uint8(if_gaus)
h07 = fun.my_hist(Im_07)
plt.figure()
plt.bar(np.arange(256),h07)
plt.title("Histograma imagen 0.7")






