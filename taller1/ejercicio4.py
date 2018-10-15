# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:43:49 2018

@author: Manuel Andres Sanchez Muñoz

Ejercicio 4

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('rain.jpg').convert('RGB')
plt.figure()
plt.gray()
plt.imshow(image)

imageA = np.array(image)
returnImage = fun.rgb2ycbcr(imageA)
plt.figure()
plt.gray()  
plt.imshow(returnImage)

returnImage2 = fun.ycbcr2rgb(returnImage)
Viewimage = np.uint8(returnImage2)
plt.figure()
plt.gray()
plt.imshow(Viewimage)   

Viewimagedouble = np.double(Viewimage)
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




