# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:40:53 2018

@author: Manuel Andres Sanchez Muñoz

Ejercicio 1

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun
    
x = np.array([0.05, 0.10, 0.20, 0.50, 1, 1.5, 2.5, 5.0, 10.0, 25.0])

Im_g = Image.open('fruit.jpg').convert('L')

for i in x:
    A = i    
    Im_ga = np.array(Im_g)
    imageList = fun.my_gamma(Im_ga, A)
    plt.figure()
    plt.gray()
    plt.imshow(imageList)















