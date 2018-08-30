# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:43:49 2018

@author: Manuel Sanchez

Ejercicio 4

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('pantain.jpg').convert('RGB')
plt.figure()
plt.gray()
plt.imshow(image)

doubleImage = np.double(image)

returnImage = fun.rgb2ycbcr(doubleImage)
plt.figure()
plt.gray()
plt.imshow(returnImage)

returnImage2 = fun.ycbcr2rgb(returnImage)
Viewimage = np.uint8(returnImage2)
plt.figure()
plt.gray()
plt.imshow(Viewimage)

