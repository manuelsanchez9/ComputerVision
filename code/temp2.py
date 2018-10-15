# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/media/mariatorres/ADATA UFD/VAI92/Code/')
import my_linealT as trans 

Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.array(Im_g)
a = np.array([1, 1, 1])
p1 = np.array([50, 125])
p2 = np.array([200, 225])
Im2 = trans.my_linealTrozos(Im_ga,a,p1,p2)

plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.axis("off")

plt.figure()
plt.gray()
plt.imshow(Im2)
plt.axis("off")

