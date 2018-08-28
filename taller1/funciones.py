# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:39:39 2018

@author: Manuel Sanchez

Funciones

"""
import numpy as np

def my_gamma(image,gamma):
    Im_ga = np.double(image)
    Im2 = Im_ga**gamma #gamma image
    Im2 = np.uint8(255*Im2/Im2.max())
    return Im2

def grayWhite(image, A, B):
    imageArray = np.array(image)
    returnArray = []
    
    for i in imageArray:
        for j in i:
             if (j >= A and j <= B):
                returnArray.append(0)
             else:
                returnArray.append(1)                
    return returnArray

def grayBlack(image, A, B):
    imageArray = np.array(image)
    returnArray = []
    
    for i in imageArray:
        for j in i:
             if (j >= A and j <= B):
                returnArray.append(255)
             else:
                returnArray.append(0)                
    return returnArray

def my_hist(im):
    [row, col] = im.shape;
    vec = np.zeros(256)
    print(vec.shape)
    for i in range(0,row-1):
        for j in range(0,col-1):
            valor = im[i,j] 
            vec[valor] = vec[valor] + 1
    return vec

def my_equal(im,h):
    [row, col] = im.shape;
    n = row*col
    p = h/n
    s = np.cumsum(p)
    k = s*255
    im2=im
    for i in range(0,row-1):
        for j in range(0,col-1):
            valor = im[i,j] 
            im2[i,j]=k[valor]
    return im2



