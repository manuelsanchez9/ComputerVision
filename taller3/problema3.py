# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:31:37 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import funciones as fun

Im_g = Image.open('peppers.jpg')
plt.imshow(Im_g)
plt.title('Peppers')

Im_ga = np.array(Im_g)

cmy = fun.my_cmy2rgb(Im_ga)

plt.figure()
plt.imshow(cmy)
plt.title('Peppers en CMY')

hsi = fun.rgb2hsi(Im_ga)

plt.figure()
plt.imshow(hsi)
plt.title('Peppers en HSI')

YCbCr = fun.rgb2ycbcr(Im_ga)

plt.figure()
plt.imshow(YCbCr)
plt.title('Peppers en YCbCr')

plt.figure()
Im_g = Image.open('church.jpg')
plt.imshow(Im_g)
plt.title('Church')

Im_ga = np.array(Im_g)

cmy = fun.my_cmy2rgb(Im_ga)

plt.figure()
plt.imshow(cmy)
plt.title('Church en CMY')

hsi = fun.rgb2hsi(Im_ga)

plt.figure()
plt.imshow(hsi)
plt.title('Church en HSI')

YCbCr = fun.rgb2ycbcr(Im_ga)

plt.figure()
plt.imshow(YCbCr)
plt.title('Church en YCbCr')

plt.figure()
Im_g = Image.open('bear.jpg')
plt.imshow(Im_g)
plt.title('Bear')

Im_ga = np.array(Im_g)

cmy = fun.my_cmy2rgb(Im_ga)

plt.figure()
plt.imshow(cmy)
plt.title('Bear en CMY')

hsi = fun.rgb2hsi(Im_ga)

plt.figure()
plt.imshow(hsi)
plt.title('Bear en HSI')

YCbCr = fun.rgb2ycbcr(Im_ga)

plt.figure()
plt.imshow(YCbCr)
plt.title('Bear en YCbCr')


