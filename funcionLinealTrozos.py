# -*- coding: utf-8 -*-
"""
Creada el lunes 2018-08-20

Función lineal a trozos

Autores: Getulio Rafael Vargas Sierra
         Juan Fernando Roldán Galeano
"""

import numpy as np

def funcionLinealTrozos(image, A, B):
    arrayImage = np.array(image)
    arrayResponse = []
    
    for i in arrayImage:
        for j in i:
             if (j >= A and j <= B):
                arrayResponse.append(0)
             else:
                arrayResponse.append(1)
                
    return arrayResponse