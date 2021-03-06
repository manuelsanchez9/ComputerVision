#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:44:10 2018

@author: mariatorres
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters

Im_g = Image.open('noise1.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

Im_f1 = filters.uniform_filter(Im_ga,11)
plt.figure()
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
