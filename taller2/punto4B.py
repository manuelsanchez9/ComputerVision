# -*- coding: utf-8 -*-
"""
Created on Sat Oct 06 19:53:35 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('opaca.jpg').convert('RGB')
plt.figure()
plt.gray()
plt.imshow(image)
plt.title('Imagen Original')

Viewimagedouble = np.double(image)
returnImage3 = fun.rgb2ycbcr(Viewimagedouble)
Y =  returnImage3[:,:,0]
Yi = np.uint8(255*Y/Y.max())
h = fun.my_hist(Yi)
Yeq = fun.my_equal(Yi, h)
returnImage3[:,:,0] = Yeq
sendImage = np.double(returnImage3)
previousImage = fun.ycbcr2rgb(sendImage)
finalImage = np.uint8(previousImage)
plt.figure()
plt.gray()
plt.imshow(finalImage)
plt.title('Imagen Ecualizada YcbCr')