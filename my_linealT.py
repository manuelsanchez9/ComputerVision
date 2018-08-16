# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:11:47 2018

@author: Analistad
"""

import numpy as np

def my_gamma(image, gamma):
    Im_ga = np.double(image)
    Im2 = Im_ga**gamma #gamma image
    Im2 = np.uint8(255*Im2/Im2.max())
    return Im2
