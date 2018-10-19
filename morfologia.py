# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:40:51 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg',0)
plt.imshow(img,cmap = 'gray')
plt.title('Imagen Original en Escala de Grises')

ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(255-thresh1,cmap = 'gray')
plt.title('Imagen Pasada por THRESHOLD')

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(255-thresh1,kernel,iterations = 1)
dilation = cv2.dilate(255-thresh1,kernel,iterations = 1)
opening = cv2.morphologyEx(255-thresh1,cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(255-thresh1,cv2.MORPH_CLOSE, kernel)

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