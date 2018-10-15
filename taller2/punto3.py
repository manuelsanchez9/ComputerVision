# -*- coding: utf-8 -*-
"""
Created on Sat Oct 06 19:50:31 2018

@author: Manuel Andres Sanchez Muñoz
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import funciones as fun

Im = Image.open('fruit.jpg').convert('RGB')
Im_a = np.array(Im)
plt.figure()
plt.imshow(Im_a)
plt.title('Imagen Original RGB')

plt.figure()
plt.imshow(Im_a[:,:,0],cmap='gray')
plt.title('Imagen en canal R')

plt.figure()
plt.imshow(Im_a[:,:,1],cmap='gray')
plt.title('Imagen en canal G')

plt.figure()
plt.imshow(Im_a[:,:,2],cmap='gray')
plt.title('Imagen en canal B')

Im_cmy = fun.my_rgb2cmy(Im_a)
plt.figure()
plt.imshow(Im_cmy)
plt.title('Imagen Original CMY')

plt.figure()
plt.imshow(Im_cmy[:,:,0],cmap='gray')
plt.title('Imagen en canal C')

plt.figure()
plt.imshow(Im_cmy[:,:,1],cmap='gray')
plt.title('Imagen en canal M')

plt.figure()
plt.imshow(Im_cmy[:,:,2],cmap='gray')
plt.title('Imagen en canal Y')