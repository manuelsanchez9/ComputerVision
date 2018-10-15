
#!/usr/bin/env python3
import numpy as np
import scipy.signal as sg

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

def my_mse(image1,image2):
    [n,l]=image1.shape
    n = n*l
    mse = sum(sum((image1-image2)**2))/n    
    return mse

def my_medianfilter(im):
    [row,col]=im.shape
    imf = np.zeros((row+2,col+2))
    i_median = np.zeros((row,col))
    imf[1:row+1,1:col+1]=im
    for i in range(1,row):
        for j in range(1,col):
            temp = imf[i-1:i+1,j-1:j+1]
            out = np.median(temp)
            i_median[i-1,j-1]=out
    return i_median

def my_gradient(im):
    mask_dx = np.array([(-1,-2,-1),(0,0,0),(1,2,1)])
    mask_dy = np.array([(-1,0,1),(-2,0,2),(-1,0,1)])
    Im_dx = sg.convolve2d(im,mask_dx)
    Im_dy = sg.convolve2d(im,mask_dy)
    Im_grad = np.abs(Im_dx)+np.abs(Im_dy)
    return (Im_grad,Im_dx,Im_dy)

    
    







