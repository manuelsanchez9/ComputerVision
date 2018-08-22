# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import my_linealT as trans 

Im_g = Image.open('img1.jpg').convert('L')
Im_ga = np.array(Im_g)
Im2 = trans.my_gamma(Im_ga,2)

plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.axis("off")

plt.figure()
plt.gray()
plt.imshow(Im2)
plt.axis("off")

