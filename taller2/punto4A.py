# -*- coding: utf-8 -*-
"""
Created on Mon Oct 08 07:39:09 2018

@author: Manuel Andres Sanchez Muñoz
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import funciones as fun

Im = Image.open('opaca.jpg').convert('RGB')
Im_a = np.array(Im)
plt.imshow(Im_a)
plt.title("Imagen Original")


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

I = imageHSI[:,:,2]
Inew = np.uint8(255*I/I.max())
hist = fun.my_hist(Inew)
Iequal = fun.my_equal(Inew, hist)

imageHSI[:,:,2] = Iequal
        
ch = imageHSI[:,:,0]
cs = imageHSI[:,:,1]
ci = imageHSI[:,:,2]

for i in range(0,row-1):
    for j in range(0,col-1):
        [R,G,B] = fun.rgb2hsi(ch[i][j], cs[i][j], ci[i][j])
        r[i][j] = R*255
        g[i][j] = G*255
        b[i][j] = B*255
         
Im_a[:,:,0] = r
Im_a[:,:,1] = g
Im_a[:,:,2] = b
        
Im_view = np.uint8(Im_a)
plt.figure()
plt.imshow(Im_view)
plt.title("Imagen RGB desde HSI - I equalizado")
