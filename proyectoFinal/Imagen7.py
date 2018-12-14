# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:35:01 2018

@author: Manuel Andres Sanchez Muñoz
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

img = cv2.imread('img7.jpg')
[nf,nc,nb] = img.shape
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
N=9
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