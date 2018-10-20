# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:44:38 2018

@author: Manuel Sanchez
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters

Im_g = Image.open('img3.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)

Im_f1 = filters.uniform_filter(Im_ga,3)
plt.figure()
plt.gray()
plt.imshow(Im_f1)
