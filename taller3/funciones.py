# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:39:39 2018

@author: Manuel Andres Sanchez Muñoz

Funciones

"""
import numpy as np
import scipy.signal as sg
import cv2

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

def my_laplace_4_vecinos(im):
    mask_dx = np.array([(0,-1,0),(-1,5,-1),(0,-1,0)])
    Im_dx = sg.convolve2d(im,mask_dx)
    imageReturn = np.uint8(255*Im_dx/Im_dx.max())
    return (imageReturn)

def my_laplace_8_vecinos(im):
    mask_dx = np.array([(-1,-1,-1),(-1,9,-1),(-1,-1,-1)])
    Im_dx = sg.convolve2d(im,mask_dx)
    imageReturn = np.uint8(255*Im_dx/Im_dx.max())
    return (imageReturn)

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

def my_threshold(image, umbral):
    Image_lt = np.double(image)
    Image_zero = np.zeros(Image_lt.shape)
    Image_zero[(Image_lt>=umbral)]=1
    imageResponse = np.uint8(Image_zero)
    return imageResponse    

def rgb2hsi(im):
    HSI = np.double(np.zeros(im.shape))
    R = np.double(im[:,:,0]/255)
    G = np.double(im[:,:,1]/255)
    B = np.double(im[:,:,2]/255)
    ## Computing H
    num = 0.5*((R-G)+(R-B))
    den = ((R-G)**2+(R-B)*(G-B))**0.5+1/100000000000
    theta = np.arccos(num/den)
    temp = np.copy(theta)
    temp[B>G]=2*np.pi-theta[B>G]
    HSI[:,:,0]=temp
    ## Computing S
    temp = np.min([R,G,B],axis=0)
    HSI[:,:,1]=1-3*temp/(R+G+B)
    ## Computing I
    HSI[:,:,2]=(R+G+B)/3
    return HSI

def hsi2rgb (HSI):
    [nf,nc,nb]=HSI.shape
    RGB = np.double(np.zeros(HSI.shape))
    H = HSI[:,:,0]
    S = HSI[:,:,1]
    I = HSI[:,:,2]
    tempR = np.zeros((nf,nc))
    tempG = np.zeros((nf,nc))
    tempB = np.zeros((nf,nc))
    ## Computing RG sector
    tempB[(H>=0)&(H<=(2*np.pi/3))]=I[(H>=0)&(H<=(2*np.pi/3))]*(1-S[(H>=0)&(H<=(2*np.pi/3))])
    tempR[(H>=0)&(H<=(2*np.pi/3))]=I[(H>=0)&(H<=(2*np.pi/3))]*(1+S[(H>=0)&(H<=(2*np.pi/3))]*np.cos(H[(H>=0)&(H<=(2*np.pi/3))])/np.cos(np.pi/3-H[(H>=0)&(H<=(2*np.pi/3))]))
    tempG[(H>=0)&(H<=(2*np.pi/3))]=3*I[(H>=0)&(H<=(2*np.pi/3))]-(tempR[(H>=0)&(H<=(2*np.pi/3))]+tempB[(H>=0)&(H<=(2*np.pi/3))])
    ## Computing GB sector
    tempR[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]=I[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]*(1-S[(H>(2*np.pi/3))&(H<=(4*np.pi/3))])
    tempG[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]=I[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]*(1+S[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]*np.cos(H[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]-2*np.pi/3)/np.cos(np.pi/3-(H[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]-2*np.pi/3)))
    tempB[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]=3*I[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]-(tempR[(H>(2*np.pi/3))&(H<=(4*np.pi/3))]+tempG[(H>(2*np.pi/3))&(H<=(4*np.pi/3))])
    ## Computing GB sector
    tempG[(H>(4*np.pi/3))&(H<=(2*np.pi))]=I[(H>(4*np.pi/3))&(H<=(2*np.pi))]*(1-S[(H>(4*np.pi/3))&(H<=(2*np.pi))])   
    tempB[(H>(4*np.pi/3))&(H<=(2*np.pi))]=I[(H>(4*np.pi/3))&(H<=(2*np.pi))]*(1+S[(H>(4*np.pi/3))&(H<=(2*np.pi))]*np.cos(H[(H>(4*np.pi/3))&(H<=(2*np.pi))]-4*np.pi/3)/np.cos(np.pi/3-(H[(H>(4*np.pi/3))&(H<=(2*np.pi))]-4*np.pi/3)))
    tempR[(H>(4*np.pi/3))&(H<=(2*np.pi))]=3*I[(H>(4*np.pi/3))&(H<=(2*np.pi))]-(tempG[(H>(4*np.pi/3))&(H<=(2*np.pi))]+tempB[(H>(4*np.pi/3))&(H<=(2*np.pi))])
    ##
    RGB[:,:,0]=tempR*255
    RGB[:,:,1]=tempG*255
    RGB[:,:,2]=tempB*255
    RGB = np.uint8(RGB)
    return RGB

def frontera(img):
    ret,thresh1 = cv2.threshold(255-img,190,255,cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(255-thresh1,kernel,iterations = 1)
    imgFrontera = (255-thresh1) - erosion  
    return imgFrontera
        
        
        
        

            
        
    
    
    
    
    
    



