# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
#Librería necesaria para extraer el texto de una imagen
from pytesseract import image_to_string

def loadImageGray(imageName):
    imageLoaded = Image.open(imageName).convert('L')
    responseImage = np.array(imageLoaded)
    return responseImage

def loadImageRGB(imageName):
    imageLoaded = Image.open(imageName).convert('RGB')
    responseImage = np.array(imageLoaded)
    return responseImage

def showImage(image, title):
    plt.gray()
    plt.figure()
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def my_hist(im):
    [row, col] = im.shape;
    vec = np.zeros(256)
    print(vec.shape)
    for i in range(0,row-1):
        for j in range(0,col-1):
            valor = im[i,j] 
            vec[valor] = vec[valor] + 1
    return vec

def showHist(hist, title):
    plt.figure()
    plt.bar(np.arange(256), hist)
    plt.title(title)

def my_rgb2cmy(im):
    CMY = 255 - im
    return CMY

def my_cmy2rgb(im):
    RGB = 255 - im
    return RGB

def rgb2ycbcr(image):
    xform = np.array([[.299, .587, .114], [-.169, -.331, .5], [.5, -.419, -.081]])
    ycbcr = image.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.double(ycbcr)

def ycbcr2rgb(image):
    xform = np.array([[1, 0, 1.403], [1, -0.344, -.714], [1, 1.773, 0]])
    rgb = image.astype(np.float)
    rgb[:,:,[1,2]] -= 128
    rgb = rgb.dot(xform.T)
    np.putmask(rgb, rgb > 255, 255)
    np.putmask(rgb, rgb < 0, 0)
    return np.uint8(rgb)

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

"""Convierte una imagen en binaria; es decir, en unos y ceros. Donde 1 es blanco y 0 es negro"""
def realceRangoGrises(image, A, B):
    Image_lt = np.double(image)
    Image_zero = np.zeros(Image_lt.shape)
    Image_zero[(Image_lt>=A)&(Image_lt<=B)]=255
    imageResponse = np.uint8(Image_zero)
    return imageResponse

"""Obtener el borde de una imagen"""
def frontera(image, kernel):
    ret,threshold = cv2.threshold(255-image,190,255,cv2.THRESH_BINARY)
    imgErosion = cv2.erode(255-threshold,kernel,iterations = 1)
    imgFrontera = (255-threshold) - imgErosion
    return imgFrontera

def myThreshold(image, umbral):
    Image_lt = np.double(image)
    Image_zero = np.zeros(Image_lt.shape)
    Image_zero[(Image_lt>=umbral)]=1
    imageReturn = np.uint8(Image_zero)
    return imageReturn

"""Función encargada de recibir una imagen 'limpia' y extraer el texto de esta"""
def getStringFromImage(image):
    responseText = image_to_string(image)
    return responseText

"""Función que se encarga de contar las palabras de un texto enviado y retornar esta cantidad"""
def getQuantityWords(text):
    textConverted = text.replace('\n', ' ')
    textArray = textConverted.split(' ')
    quantity = 0
    
    for i in textArray:
        if (len(i) > 0):
            quantity = quantity + 1
    
    return quantity

"""Función que se encarga de contar los caracteres de un texto determinado"""
def getQuantityCharacters(text):
    textConverted = text.replace('\n', '')
    textConverted = textConverted.replace(' ', '')
    
    return len(textConverted)