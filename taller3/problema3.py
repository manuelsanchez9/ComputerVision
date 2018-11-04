# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:31:37 2018

@author: Manuel Andres Sanchez Muñoz
"""

#primera imagen

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import funciones as fun
import cv2

Im_g = Image.open('peppers.jpg')
plt.imshow(Im_g)
plt.title('Peppers en RGB')

Im_ga = np.array(Im_g)

cmy = fun.my_rgb2cmy(Im_ga)

plt.figure()
plt.imshow(cmy)
plt.title('Peppers en CMY')

plt.figure()
cmy = cv2.imread('cmy.jpg',0)
plt.imshow(cmy, cmap = 'gray')
plt.title('Peppers en CMY y en Escala de Grises')

h = fun.my_hist(cmy)
plt.figure()
plt.bar(np.arange(256),h)
plt.title("Histograma Peppers en Escala de Grises")

ret,thresh1 = cv2.threshold(cmy,195,200,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(255-thresh1,cmap = 'gray')
plt.title('Peppers Separa Objeto de Interes')

Datos = np.uint8(thresh1)

acumuladorMatriz = float(0);
suma = 0
suma1 = 0

for x in Datos:
    acumuladorFilas = float(0);
    acumuladorColumnas = float(0);
    
    for y in x:        
        acumuladorFilas = acumuladorFilas + Datos[0][0];
        acumuladorColumnas = acumuladorColumnas + Datos[0][0];
        
        if (y >= 199 and y <= 200):
                cont =+ 1
                suma = suma + cont
        else:
            cont1 =+ 1
            suma1 = suma1 + cont1

print ("El numero de elementos iguales a 1 para peppers.jpg binario es: " + str(suma))
print ("El numero de elementos iguales a 0 para peppers.jpg binario es: " + str(suma1))

hsi = fun.rgb2hsi(Im_ga)

plt.figure()
plt.imshow(hsi)
plt.title('Peppers en HSI')

YCbCr = fun.rgb2ycbcr(Im_ga)

plt.figure()
plt.imshow(YCbCr)
plt.title('Peppers en YCbCr')

#segunda imagen

plt.figure()
Im_g = Image.open('church.jpg')
plt.imshow(Im_g)
plt.title('Church en RGB')

plt.figure()
Im = cv2.imread('church.jpg',0)
plt.imshow(Im, cmap = 'gray')
plt.title('Church en Escala de Grises')

h = fun.my_hist(Im)
plt.figure()
plt.bar(np.arange(256),h)
plt.title("Histograma Church en Escala de Grises")

ret,thresh1 = cv2.threshold(Im,170,225,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh1,cmap = 'gray')
plt.title('Church Separa Objeto de Interes')

Datos = np.uint8(thresh1)

acumuladorMatriz = float(0);
suma = 0
suma1 = 0

for x in Datos:
    acumuladorFilas = float(0);
    acumuladorColumnas = float(0);
    
    for y in x:        
        acumuladorFilas = acumuladorFilas + Datos[0][0];
        acumuladorColumnas = acumuladorColumnas + Datos[0][0];
        
        if (y >= 224 and y <= 225):
                cont =+ 1
                suma = suma + cont
        else:
            cont1 =+ 1
            suma1 = suma1 + cont1

print ("El numero de elementos iguales a 1 para church.jpg binario es: " + str(suma))
print ("El numero de elementos iguales a 0 para church.jpg binario es: " + str(suma1))

Im_ga = np.array(Im_g)

cmy = fun.my_rgb2cmy(Im_ga)

plt.figure()
plt.imshow(cmy)
plt.title('Church en CMY')

hsi = fun.rgb2hsi(Im_ga)

plt.figure()
plt.imshow(hsi)
plt.title('Church en HSI')

YCbCr = fun.rgb2ycbcr(Im_ga)

plt.figure()
plt.imshow(YCbCr)
plt.title('Church en YCbCr')

#tercera imagen

plt.figure()
Im_g = Image.open('bear.jpg')
plt.imshow(Im_g)
plt.title('Bear en RGB')

plt.figure()
Im = cv2.imread('bear.jpg',0)
plt.imshow(Im, cmap = 'gray')
plt.title('Bear en Escala de Grises')

h = fun.my_hist(Im)
plt.figure()
plt.bar(np.arange(256),h)
plt.title("Histograma Bear en Escala de Grises")

ret,thresh1 = cv2.threshold(255-Im,110,160,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh1,cmap = 'gray')
plt.title('Bear Separa Objeto de Interes')

Datos = np.uint8(thresh1)

acumuladorMatriz = float(0);
suma = 0
suma1 = 0

for x in Datos:
    acumuladorFilas = float(0);
    acumuladorColumnas = float(0);
    
    for y in x:        
        acumuladorFilas = acumuladorFilas + Datos[0][0];
        acumuladorColumnas = acumuladorColumnas + Datos[0][0];
        
        if (y >= 159 and y <= 160):
                cont =+ 1
                suma = suma + cont
        else:
            cont1 =+ 1
            suma1 = suma1 + cont1

print ("El numero de elementos iguales a 1 para bear.jpg binario es: " + str(suma))
print ("El numero de elementos iguales a 0 para bear.jpg binario es: " + str(suma1))

Im_ga = np.array(Im_g)

cmy = fun.my_cmy2rgb(Im_ga)

plt.figure()
plt.imshow(cmy)
plt.title('Bear en CMY')

hsi = fun.rgb2hsi(Im_ga)

plt.figure()
plt.imshow(hsi)
plt.title('Bear en HSI')

YCbCr = fun.rgb2ycbcr(Im_ga)

plt.figure()
plt.imshow(YCbCr)
plt.title('Bear en YCbCr')


