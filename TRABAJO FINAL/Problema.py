# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:09:36 2018

@author: Manuel Sanchez Muñoz
         Juan Roldán Galeano
         Getulio Vargas Sierra
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
from PIL import Image
from pytesseract import image_to_string
import generalFunctions as fun

pathImage = "Images/test.jpg"

imageGray = fun.loadImageGray(pathImage)
texto = fun.getStringFromImage(imageGray)
print ("El texto de la imagen es: ")
print ("-----------------------------------------")
print (texto)
print ("-----------------------------------------")
quantityWords = fun.getQuantityWords(texto)
print ("La cantidad de palabras de la imagen es: " + str(quantityWords))
print ("-----------------------------------------")
quantityCharacters = fun.getQuantityCharacters(texto)
print ("La cantidad de caracteres de la imagen es: " + str(quantityCharacters))