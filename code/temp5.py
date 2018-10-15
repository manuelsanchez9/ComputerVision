#!/usr/bin/env python3
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters
Im_g = Image.open('noise1.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

Im_f1 = filters.uniform_filter(Im_ga,5)
plt.figure()
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("Filtro uniforme")

Im_f2 = filters.gaussian_filter(Im_ga,1)
plt.figure()
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro Gaussiano")
