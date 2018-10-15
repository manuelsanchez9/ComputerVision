# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:50:58 2018

@author: Manuel Andres Sanchez Muñoz
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import funciones as fun

Im = Image.open('fruit.jpg').convert('RGB')
Im_a = np.array(Im)
plt.figure()
plt.imshow(Im_a)
plt.title('Imagen Original RGB')

[row, col, ch] = Im_a.shape

imageD = np.double(Im_a)/255

r = imageD[:,:,0]
g = imageD[:,:,1]
b = imageD[:,:,2]

ch = np.zeros([row,col])
cs = np.zeros([row,col])
ci = np.zeros([row,col])

imageHSI = np.zeros(Im_a.shape)

for i in range(0,row-1):
    for j in range(0,col-1):
        [H,S,I] = fun.rgb2hsi(r[i][j], g[i][j], b[i][j])
        ch[i][j] = H
        cs[i][j] = S
        ci[i][j] = I
    
imageHSI[:,:,0] = ch
imageHSI[:,:,1] = cs
imageHSI[:,:,2] = ci

plt.figure()
plt.imshow(imageHSI[:,:,0],cmap='gray')
plt.title('Imagen en canal H')

plt.figure()
plt.imshow(imageHSI[:,:,1],cmap='gray')
plt.title('Imagen en canal S')

plt.figure()
plt.imshow(imageHSI[:,:,2],cmap='gray')
plt.title('Imagen en canal I')
        
plt.figure()
plt.imshow(imageHSI)
plt.title('Imagen HSI')

ch = imageHSI[:,:,0]
cs = imageHSI[:,:,1]
ci = imageHSI[:,:,2]

for i in range(0,row-1):
    for j in range(0,col-1):
        [R,G,B] = fun.hsi2rgb(ch[i][j], cs[i][j], ci[i][j])
        r[i][j] = R*255
        g[i][j] = G*255
        b[i][j] = B*255
         
Im_a[:,:,0] = r
Im_a[:,:,1] = g
Im_a[:,:,2] = b
           
plt.figure()
plt.imshow(Im_a)
plt.title('Imagen Original RGB')

mse_f1 = fun.my_mseRGB(Im_a,Im_a)

print ("MSE entre imagen original e imagen que paso por el espacio HSI: " 
       + str(mse_f1))


