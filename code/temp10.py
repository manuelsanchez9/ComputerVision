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


Im = Image.open('build.jpg')
Im_a = np.array(Im)
Im_cmy = fun.my_rgb2cmy(Im_a)
Im_rgb = fun.my_cmy2rgb(Im_cmy)

plt.subplot(131)
plt.imshow(Im_a)
plt.axis("off")
plt.subplot(132)
plt.imshow(Im_cmy)
plt.axis("off")
plt.subplot(133)
plt.imshow(Im_rgb)
plt.axis("off")

plt.figure()
plt.subplot(231)
plt.imshow(Im_a[:,:,0], cmap='gray')
plt.axis("off")
plt.subplot(232)
plt.imshow(Im_a[:,:,1], cmap='gray')
plt.axis("off")
plt.subplot(233)
plt.imshow(Im_a[:,:,2], cmap='gray')
plt.axis("off")

plt.subplot(234)
plt.imshow(Im_cmy[:,:,0], cmap='gray')
plt.axis("off")
plt.subplot(235)
plt.imshow(Im_cmy[:,:,1], cmap='gray')
plt.axis("off")
plt.subplot(236)
plt.imshow(Im_cmy[:,:,2], cmap='gray')
plt.axis("off")




