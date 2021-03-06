# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:42:36 2018

@author: Manuel Andres Sanchez Muñoz

Ejercicio 2

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('fruit.jpg').convert('L')
imageArray = np.array(image)
plt.gray()
plt.imshow(np.uint8(imageArray))
values = [(20,240),(40,200),(80,180),(100,150),(120,135)]

for i in values:
    A = i[0]
    B = i[1]
    sendImage = fun.grayWhite(image, A, B)
    plt.figure()
    plt.gray()
    plt.imshow(sendImage)