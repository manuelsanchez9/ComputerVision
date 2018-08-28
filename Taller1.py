# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:40:53 2018

@author: Manuel Andres Sanchez


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import my_linealT as trans
Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.array(Im_g)
Im2 = trans.my_gamma(Im_ga, 0.05)
plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.figure()
plt.gray()
Im = Image.fromarray(Im2)
Im.save('img2250.jpg')
plt.imshow(Im2)
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

A = 20
B = 240

Im = Image.open('img2.jpg').convert('L')
Im_a = np.array(Im)
Im_d = np.double(Im_a)
#Im_z = np.zeros(Im_d.shape)

print (Im_d[0,0])











