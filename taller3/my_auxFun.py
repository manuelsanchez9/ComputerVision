
#!/usr/bin/env python3
import numpy as np
import scipy.signal as sg

def my_RGB2HSI(im):
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

def my_HSI2RGB(HSI):
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

def my_rgb2YCbCr(im):
    YCbCr = np.double(np.zeros(im.shape))
    R = im[:,:,0]
    G = im[:,:,1]
    B = im[:,:,2]
    YCbCr[:,:,0] = 0.299*R+0.587*G+0.114*B
    YCbCr[:,:,1] = -0.169*R-0.331*G+0.500*B+128
    YCbCr[:,:,2] = 0.500*R-0.419*G-0.081*B+128
    return YCbCr

def my_YCbCr2RGB(YCbCr):
    RGB = np.zeros(YCbCr.shape)
    Y = YCbCr[:,:,0]
    Cb = YCbCr[:,:,1]
    Cr = YCbCr[:,:,2]
    RGB[:,:,0] = Y+1.403*(Cr-128)
    RGB[:,:,1] = Y-0.344*(Cb-128)-0.714*(Cr-128)
    RGB[:,:,2] = Y+1.773*(Cb-128)
    RGB = np.uint8(255*RGB/255)
    return RGB

def my_equalRGB_HSI(im):
    HSI = my_RGB2HSI(im)
    I = HSI[:,:,2]
    I = np.uint8(255*I)
    h = my_hist(I)
    Ieq = my_equal(I,h)
    HSI[:,:,2]=np.double(Ieq/255)
    RGB = my_HSI2RGB(HSI)
    return RGB

def my_equalRGB(im):
    YCbCr = my_rgb2YCbCr(im)
    Y = YCbCr[:,:,0]
    Y = np.uint8(255*Y/255)
    h = my_hist(Y)
    Yeq = my_equal(Y,h)
    YCbCr[:,:,0]=np.double(Yeq)
    RGB = my_YCbCr2RGB(YCbCr)
    return RGB
    
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

    
    







