#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:44:10 2018

@author: mariatorres
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import my_auxFun as myf
from scipy.ndimage import filters

Im = Image.open('build.jpg')
Im_a = np.array(Im)
plt.imshow(Im_a)
plt.axis("off")

[row, col, nb] = Im_a.shape
Im_n = np.zeros(Im_a.shape)
Im_n = Im_a+125*np.random.rand(row,col,nb)
Im_n = np.uint8(255*Im_n/Im_n.max())
plt.figure()
plt.imshow(Im_n)
plt.axis("off")

Im_f1 = filters.uniform_filter(Im_n,3)
plt.figure()
plt.imshow(Im_f1)
plt.axis("off")
mse_f1 = myf.my_mseRGB(Im_a,Im_f1)
plt.title(mse_f1)
  
Im_f2 = filters.gaussian_filter(Im_n,1)
plt.figure()
plt.imshow(Im_f2)
plt.axis("off")
mse_f2 = myf.my_mseRGB(Im_a,Im_f2)
plt.title(mse_f2)




