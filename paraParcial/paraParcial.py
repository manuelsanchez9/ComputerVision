# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:38:30 2018

@author: Manuel Sanchez
"""

#para llamar a la funcion logaritmo
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('img2.jpg').convert('L')
sendImage = fun.logarithm(image)

plt.gray()
plt.imshow(np.uint8(image))
plt.figure()

plt.gray()
plt.imshow(sendImage)

#para llamar a la funcion Gamma(se envian varios parametros)
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun
    
x = np.array([0.05, 0.10, 0.20, 0.50, 1, 1.5, 2.5, 5.0, 10.0, 25.0])

Im_g = Image.open('img2.jpg').convert('L')

for i in x:
    A = i    
    Im_ga = np.array(Im_g)
    imageList = fun.my_gamma(Im_ga, A)
    
    plt.figure()
    plt.gray()
    plt.imshow(imageList)
    
#para llamar las funciones RGB2YCBCR y YCBCR2RGB
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('img2.jpg').convert('RGB')
plt.figure()
plt.gray()
plt.imshow(image)

doubleImage = np.double(image)

returnImage = fun.rgb2ycbcr(doubleImage)
plt.figure()
plt.gray()
plt.imshow(returnImage)

returnImage2 = fun.ycbcr2rgb(returnImage)
Viewimage = np.uint8(returnImage2)
plt.figure()
plt.gray()
plt.imshow(Viewimage)
   
#para llamar las funciones del histograma y la equalizacion
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)

h = fun.my_hist(Im_ga)
plt.figure()
plt.bar(np.arange(256),h)

Im_eq = fun.my_equal(Im_ga,h)
plt.figure()
plt.gray()
plt.imshow(Im_eq)
h1 = fun.my_hist(Im_eq)
plt.figure()
plt.bar(np.arange(256),h1)

#para llamar la funcion de fraccionamiento nivel de gris (se envian varios parametros)
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('img2.jpg').convert('L')
imageArray = np.array(image)
plt.gray()
plt.imshow(np.uint8(imageArray))
values = [(20,240),(40,200),(80,180),(100,150),(120,135)]
    
for i in values:
    A = i[0]
    B = i[1]
    sendImage = fun.grayBlack(image, A, B)
    plt.figure()
    plt.gray()
    plt.imshow(sendImage)
    
#para llamar funcion negativa
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

image = Image.open('fruit.jpg').convert('L')
imagePrint = np.array(image)
plt.figure()
plt.imshow(imagePrint)
imageView = fun.negative(image)
plt.figure()
plt.imshow(imageView)

#para llamar la funcion lineal a trozos
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import funciones as fun 

Im_g = Image.open('fruit.jpg').convert('L')
Im_ga = np.array(Im_g)
a = np.array([1, 1, 1])
p1 = np.array([50, 125])
p2 = np.array([200, 225])
Im2 = fun.my_linealTrozos(Im_ga,a,p1,p2)

plt.gray()
plt.imshow(np.uint8(Im_ga))

plt.figure()
plt.gray()
plt.imshow(Im2)

#para hacer operaciones con matrices
A = [[20,0,20],[20,1,20],[3,11,10]];
acumuladorMatriz = float(0);
suma = 0

for x in range (0,3):
    acumuladorFilas = float(0);
    acumuladorColumnas = float(0);
        
    for y in range (0,3):        
        acumuladorFilas = acumuladorFilas + A[x][y];
        acumuladorColumnas = acumuladorColumnas + A[y][x];
        
        if A[x][y] >= 10:
            cont =+ 1
            suma = suma + cont  
            
    acumuladorMatriz = acumuladorMatriz + acumuladorFilas; 
        
#    print("La suma de la fila " + str(x + 1) + " es de: " + str(acumuladorFilas))
    print("La suma de la columna " + str(x + 1) + " es de: " + str(acumuladorColumnas))
    print("El promedio de la fila " + str(x + 1) + " es de: " + str(acumuladorFilas/3));
#    print("El promedio de la columna " + str(x + 1) + " es de: " + str(acumuladorColumnas/3))
#print("El promedio de toda la matriz es de: " + str(acumuladorMatriz/9));
print ("El numero de elementos iguales o mayores a 10 es: " + str(suma))

#para hallar la serie geometrica 1 + r + r^2 + r^3 + ... + r^n
r = 6
s = 3
i = 0
acum = 0

while i < s:    
    i += 1
    suma = r ** i     
    acum = acum + suma
acumResult = acum + 1
print("El valor hallado es: " + str(acumResult))

