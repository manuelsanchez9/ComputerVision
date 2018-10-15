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


Im_g = Image.open('build.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

[Ig,Ix,Iy]=fun.my_gradient(Im_ga)
plt.figure()
plt.gray()
plt.imshow(Ix)
plt.axis("off")
plt.title("Derivada en x")

plt.figure()
plt.gray()
plt.imshow(Iy)
plt.axis("off")
plt.title("Derivada en y")

plt.figure()
plt.gray()
plt.imshow(Ig)
plt.axis("off")
plt.title("Gradiente")



