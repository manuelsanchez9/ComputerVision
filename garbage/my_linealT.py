#!/usr/bin/env python3
import numpy as np

def my_linealTrozos(image,a,p1,p2):
    Im_lt = np.double(image)
    Im_s = np.zeros(Im_lt.shape)
    Im_s[Im_lt<=p1[0]]=a[0]*Im_lt[Im_lt<=p1[0]]
    Im_s[(Im_lt>p1[0])&(Im_lt<=p2[0])]=a[1]*(Im_lt[(Im_lt>p1[0])&(Im_lt<=p2[0])]-p1[0])+p1[1]
    Im_s[Im_lt>p2[0]]=a[2]*(Im_lt[Im_lt>p2[0]]-p2[0])+p2[1]
    Imf = np.uint8(Im_s)
    return Imf

def my_gamma(image,gamma):
    Im_ga = np.double(image)
    Im2 = Im_ga**gamma #gamma image
    Im2 = np.uint8(255*Im2/Im2.max())
    return Im2

def my_hist(im):
    [row, col] = im.shape;
    vec = np.zeros(256)
    print(vec.shape)
    for i in range (0, row-1):
        for j in range (0, col-1):
            valor = im[i,j]
            vec[valor] = vec[valor] + 1
    return vec
        
def my_equal(im,h):
    [row, col] = im.shape;
    n = row * col
    p = h / n
    s = np.cumsum(p)
    k = s * 255
    im2 = im
    for i in range (0,row-1):
        for j in range (0,col-1):
            valor = im[i,j]
            im2[i,j] = k[valor]
    return im2
    









