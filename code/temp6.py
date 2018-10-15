#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:44:10 2018

@author: mariatorres
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import my_auxFun as fun
from scipy.ndimage import filters

Im_g = Image.open('noise2.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

[row, col] = Im_ga.shape
Im_n = np.double(Im_ga)
for i in range(0,row-1):
    for j in range(0,col-1):
        Im_n[i,j] = Im_n[i,j]+np.random.uniform(0,100)
plt.figure()
plt.gray()
plt.imshow(Im_n)
plt.axis("off")

Im_f1 = filters.uniform_filter(Im_n,5)
mse = fun.my_mse(Im_ga,Im_f1)
plt.figure()
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title(mse)
      
Im_f2 = filters.gaussian_filter(Im_n,1)
mse = fun.my_mse(Im_ga,Im_f2)
plt.figure()
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title(mse)




