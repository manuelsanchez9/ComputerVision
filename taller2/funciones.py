# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:39:39 2018

@author: Manuel Andres Sanchez Muñoz

Funciones

"""
import numpy as np
import scipy.signal as sg
from PIL import Image

def my_gamma(image,gamma):
    Im_ga = np.double(image)
    Im2 = Im_ga**gamma #gamma image
    Im2 = np.uint8(255*Im2/Im2.max())
    return Im2

def grayWhite(image, A, B):
    imageArray = np.array(image)
    zeroArray = np.zeros(imageArray.shape)
    zeroArray[(imageArray>=A)&(imageArray<=B)] = 255
    returnImage = np.uint8(zeroArray)                    
    return returnImage

def grayBlack(image, A, B):
    imageArray = np.array(image)
    imageArray[(imageArray>=A)&(imageArray<=B)] = 255                  
    returnImage = np.uint8(imageArray)                    
    return returnImage

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

def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.169, -.331, .5], [.5, -.419, -.081]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.double(ycbcr)

def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.403], [1, -0.344, -.714], [1, 1.773, 0]])
    rgb = im.astype(np.float)
    rgb[:,:,[1,2]] -= 128
    rgb = rgb.dot(xform.T)
    np.putmask(rgb, rgb > 255, 255)
    np.putmask(rgb, rgb < 0, 0)
    return np.uint8(rgb)

def my_linealTrozos(image,a,p1,p2):
    Im_lt = np.double(image)
    Im_s = np.zeros(Im_lt.shape)
    Im_s[Im_lt<=p1[0]]=a[0]*Im_lt[Im_lt<=p1[0]]
    Im_s[(Im_lt>p1[0])&(Im_lt<=p2[0])]=a[1]*(Im_lt[(Im_lt>p1[0])&(Im_lt<=p2[0])]-p1[0])+p1[1]
    Im_s[Im_lt>p2[0]]=a[2]*(Im_lt[Im_lt>p2[0]]-p2[0])+p2[1]
    Imf = np.uint8(Im_s)
    return Imf

def logarithm(image):
    imageDouble = np.double(np.array(image))
    imageReturn = np.log(1+imageDouble)
    imageReturn = np.uint8(255*imageReturn/imageReturn.max())
    return imageReturn

def negative(image):
    imageReturn = np.array(image)
    imageSend = 255 - imageReturn
    return imageSend

def my_mse(image1,image2):
    [n,l] = image1.shape
    n = n * l
    mse = sum(sum((image1-image2)**2))/n
    return mse

def my_medianfilter(im):
    [row,col]=im.shape
    imf = np.zeros((row+2,col+2))
    i_median = np.zeros((row,col))
    imf[1:row+1,1:col+1] = im
    for i in range (1,row):
        for j in range (1,col):
            temp = imf[i-1:i+1:,j-1:j+1]
            out = np.median(temp)
            i_median[i-1,j-1] = out
    return i_median

def my_gradient(im):
    mask_dx = np.array([(-1,-2,-1),(0,0,0),(1,2,1)])
    mask_dy = np.array([(-1,0,1),(-2,0,2),(-1,0,1)])
    Im_dx = sg.convolve2d(im,mask_dx)
    Im_dy = sg.convolve2d(im,mask_dy)
    Im_grad = np.abs(Im_dx)+np.abs(Im_dy)
    return (Im_grad, Im_dy, Im_dx)

def my_rgb2cmy(im):
    CMY = 255-im
    return CMY

def my_cmy2rgb(im):
    RGB = 255-im
    return RGB

def my_mseRGB(image1,image2):
    [m,n,b]=image1.shape
    N = m*n*b
    mse = sum(sum(sum((image1-image2)**2)))/N
    return mse

def my_threshold(im,umbral):
    datos=im.getdata()
    datos_binarios=[]

    for x in datos:
        if x < umbral:
            datos_binarios.append(1)
            continue
    datos_binarios.append(0)

    ibn=Image.new('1', im.size)
    ibn.putdata(datos_binarios)





