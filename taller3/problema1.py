# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 06:51:55 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import funciones as fun

img = cv2.imread('vis.jpg',0)
plt.imshow(img,cmap = 'gray')
plt.title('Imagen Original en Escala de Grises')

h = fun.my_hist(img)
plt.figure()
plt.bar(np.arange(256),h)
plt.title("Histograma de la Imagen Original en Escala de Grises")

imgGW = fun.grayWhite(img,100,255) 
plt.figure()
plt.imshow(imgGW,cmap = 'gray')
plt.title('Imagen Pasada Realce de Grises')

kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(imgGW,kernel,iterations = 1)
dilation = cv2.dilate(imgGW,kernel,iterations = 1)
opening = cv2.morphologyEx(imgGW,cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imgGW,cv2.MORPH_CLOSE, kernel)

plt.figure()
plt.subplot(221)
plt.imshow(erosion,cmap = 'gray')
plt.axis("off")
plt.title('Imagen Erosionada')

plt.subplot(222)
plt.imshow(dilation,cmap = 'gray')
plt.axis("off")
plt.title('Imagen Dilatada')

plt.subplot(223)
plt.imshow(opening,cmap = 'gray')
plt.axis("off")
plt.title('Imagen con Opening')

plt.subplot(224)
plt.imshow(closing,cmap = 'gray')
plt.axis("off")
plt.title('Imagen con Closing')

kernel2 = np.ones((5,5),np.uint8)
erosion = cv2.erode(imgGW,kernel2,iterations = 1)
dilation = cv2.dilate(imgGW,kernel2,iterations = 1)
opening = cv2.morphologyEx(imgGW,cv2.MORPH_OPEN, kernel2)
closing = cv2.morphologyEx(imgGW,cv2.MORPH_CLOSE, kernel2)

plt.figure()
plt.subplot(221)
plt.imshow(erosion,cmap = 'gray')
plt.axis("off")
plt.title('Imagen Erosionada')

plt.subplot(222)
plt.imshow(dilation,cmap = 'gray')
plt.axis("off")
plt.title('Imagen Dilatada')

plt.subplot(223)
plt.imshow(opening,cmap = 'gray')
plt.axis("off")
plt.title('Imagen con Opening')

plt.subplot(224)
plt.imshow(closing,cmap = 'gray')
plt.axis("off")
plt.title('Imagen con Closing')

imgFrontera = fun.frontera(img)  
plt.figure()
plt.imshow(imgFrontera,cmap = 'gray')
plt.title('Imagen Frontera con 3 x 3')