# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:17:09 2018

@author: Manuel Andres Sanchez Muñoz
"""

#segunda imagen

import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

img = cv2.imread('church.jpg')
[nf,nc,nb] = img.shape
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
N=3
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

Datos = np.uint8(mask)

acumuladorMatriz = float(0);
suma = 0
suma1 = 0

for x in Datos:
    acumuladorFilas = float(0);
    acumuladorColumnas = float(0);
    
    for y in x:        
        acumuladorFilas = acumuladorFilas + Datos[0][0];
        acumuladorColumnas = acumuladorColumnas + Datos[0][0];
        
        if (y >= 1 and y <= 255):
                cont =+ 1
                suma = suma + cont
        else:
            cont1 =+ 1
            suma1 = suma1 + cont1

print ("El numero de elementos iguales a 1 para bear.jpg binario es: " + str(suma))
print ("El numero de elementos iguales a 0 para bear.jpg binario es: " + str(suma1))
