#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:46:00 2018

@author: mariatorres
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

img = cv2.imread('coins.jpg')
[nf,nc,nb] = img.shape
plt.imshow(img,cmap='gray')
plt.axis('off')

img2 = np.reshape(img,(nf*nc,nb))
kmeans = KMeans(n_clusters=2, random_state=0).fit(img2)
C = kmeans.labels_

imgC = np.reshape(C,(nf,nc))
plt.figure
plt.imshow(imgC)
plt.axis('off')