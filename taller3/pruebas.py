# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 06:53:32 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import funciones as fun

img = cv2.imread('cell.jpg',0)
plt.imshow(img,cmap = 'gray')
plt.title('Imagen Original')

frontera = fun.frontera(img)

plt.figure()
plt.imshow(frontera,cmap = 'gray')
plt.title('Imagen Frontera con 3 x 3')