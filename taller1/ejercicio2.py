# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:42:36 2018

@author: Manuel Sanchez
Ejercicio 2
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#import sys
#sys.path.append('C:\Users\salak401\Desktop\ComputerVision\taller1')
import funciones as flt

imageLoaded = Image.open('fruit.jpg').convert('L')
arrayImage = np.array(imageLoaded)
plt.gray()
plt.imshow(np.uint8(arrayImage))
valuesList = [(20,240),(40,200),(80,180),(100,150),(120,135)]

for i in valuesList:
    A = i[0]
    B = i[1]
    imageList = flt.grayWhite(imageLoaded, A, B)
    imageResponse = Image.new('1', imageLoaded.size)
    imageResponse.putdata(imageList)
    plt.figure()
    plt.gray()
    plt.imshow(imageResponse)