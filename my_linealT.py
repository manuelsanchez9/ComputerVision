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

