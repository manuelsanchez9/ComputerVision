# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:51:16 2018

@author: Manuel Andres Sanchez Muñoz


a. Usaremos la morfología para aislar las células superpuestas obtenidas de un
escaneo láser confocal microscopíca. Lea la imagen cell.jpg y conviertala a 
escala de grises. Segmente las celulas usando la Función myThreshold. 
Seleccione el umbral para que las celulas puedan ser identificadas.

Incluir en el informe:    

I) Imágenes en escala de grises y binarias.
II) Una breve explicación sobre la selección del umbral.
    
b. Proponer un algoritmo morfológico que produzca dos imágenes que consistan 
respectivamente de:
    
(a) el límite de las células aisladas
(b) el límite de los grupos dentro de las células superpuestas. 

Incluya en el informe escrito:     
    
III) las imagenes obtenidas
IV) un diagrama de flujo con la operación morfológica utilizada en su marco para obtener cada imagen
V) una breve explicación sobre el algoritmo morfológico y sus resultados.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import funciones as fun

img = cv2.imread('cell.jpg',0)
plt.imshow(img,cmap = 'gray')
plt.title('Imagen Original en Escala de Grises')

h = fun.my_hist(img)
plt.figure()
plt.bar(np.arange(256),h)
plt.title("Histograma de la Imagen Original en Escala de Grises")

ret,thresh1 = cv2.threshold(img,50,175,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(255-thresh1,cmap = 'gray')
plt.title('Imagen Pasada por THRESHOLD')


