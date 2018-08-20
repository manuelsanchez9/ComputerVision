# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:40:53 2018

@author: Manuel Andres Sanchez
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import my_linealT as trans

Im_g = Image.open('fruit.jpg').convert('L')
Im_ga = np.array(Im_g)
Im2 = trans.my_gamma(Im_ga, 0.05)
plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.figure()
plt.gray()
Im = Image.fromarray(Im2)
Im.save('fruit250.jpg')
plt.imshow(Im2)