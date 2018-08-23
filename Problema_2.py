# -*- coding: utf-8 -*-
"""
Creado el lunes 2018-08-20

Autores:
    Juan Fernando Roldán Galeano
    Getulio Rafael Vargas Sierra
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import funcionLinealTrozos as flt

imageLoaded = Image.open('img_Problema_2.JPG').convert('L')
arrayImage = np.array(imageLoaded)
plt.gray()
plt.imshow(np.uint8(arrayImage))
valuesList = [(20,240),(40,200),(80,180),(100,150),(120,135)]

for i in valuesList:
    A = i[0]
    B = i[1]
    imageList = flt.funcionLinealTrozos(imageLoaded, A, B)
    imageResponse = Image.new('1', imageLoaded.size)
    imageResponse.putdata(imageList)
    plt.figure()
    plt.gray()
    plt.imshow(imageResponse)