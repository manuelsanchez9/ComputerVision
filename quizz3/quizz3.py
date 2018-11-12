# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 16:52:14 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import funciones as fun
import cv2
from sklearn.cluster import KMeans

image = Image.open('plant2n.jpg').convert('RGB')
plt.figure()
plt.gray()
plt.imshow(image)
plt.title('Imagen Original')

Viewimagedouble = np.double(image)
returnImage3 = fun.rgb2ycbcr(Viewimagedouble)
Y =  returnImage3[:,:,0]
Yi = np.uint8(255*Y/Y.max())
h = fun.my_hist(Yi)
Yeq = fun.my_equal(Yi, h)
returnImage3[:,:,0] = Yeq
sendImage = np.double(returnImage3)
previousImage = fun.ycbcr2rgb(sendImage)
finalImage = np.uint8(previousImage)
plt.figure()
plt.gray()
plt.imshow(finalImage)
plt.title('Imagen Ecualizada YcbCr')

Im_ga = np.array(finalImage)

Im_f1 = filters.uniform_filter(Im_ga,5)

plt.figure()
plt.gray()
plt.imshow(Im_f1)
plt.title("Imagen filtrada con Uniforme")

img = cv2.imread('imagen.png')
[nf,nc,nb] = img.shape
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
N=5
img2 = np.reshape(img,(nf*nc,nb))
kmeans = KMeans(n_clusters=N, random_state=0).fit(img2)
C = kmeans.labels_

imgC = np.reshape(C,(nf,nc))
plt.figure()
plt.imshow(imgC)
plt.axis('off')

for i in range(1,N):
    mask = np.zeros(imgC.shape,np.uint8)
    mask[imgC==i] = 255
    plt.figure()
    plt.imshow(mask,cmap='gray')
    plt.axis('off')  

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(255-mask,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN, kernel)

plt.figure()
plt.imshow(opening,cmap = 'gray')
plt.title('Imagen Final')








