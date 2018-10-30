#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:46:00 2018

@author: mariatorres
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg',0)
ret,thresh1 = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh1,cmap='gray')
plt.axis('off')

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh1,kernel,iterations = 2)
dilation = cv2.dilate(thresh1,kernel,iterations = 2)
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel,iterations = 2)
closing = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel,iterations = 2)
plt.figure()
plt.subplot(221)
plt.imshow(erosion,cmap = 'gray')
plt.subplot(222)
plt.imshow(dilation,cmap = 'gray')
plt.subplot(223)
plt.imshow(opening,cmap = 'gray')
plt.subplot(224)
plt.imshow(closing,cmap = 'gray')


# find contours in the thresholded image
cnts = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)[-2]
 
# loop over the contours
for (i, c) in enumerate(cnts):
	# draw the contour
	((x, y), _) = cv2.minEnclosingCircle(c)
	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

plt.figure()
plt.imshow(img,cmap='gray')
plt.axis('off')