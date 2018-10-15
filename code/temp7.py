# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import my_auxFun as myF


Im_g = Image.open('BuildSaltPepper.jpg')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

I_median = myF.my_medianfilter(Im_ga)
plt.figure()
plt.gray()
plt.imshow(I_median)
plt.axis("off")

            