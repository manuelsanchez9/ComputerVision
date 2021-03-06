# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:45:42 2018

@author: Analistad

ii = 0
while ii < 5:
    print(ii)
    ii += 1
    if ii == 1:
        break

for i in 1, 2, 4:
    print (i)

for i in range (10):
    print(i)

import numpy as np

x = np.pi
y = np.e

print(x)
print(y)

import numpy as np

x = np.array([1, 2, 3])

print (x)

N, M = 10, 10

a = np.empty(100).reshape(N, M)
b = np.random.rand(100).reshape(N, M)
c = np.random.rand(100).reshape(N, M)

a = b + c

print c

print b

print a

a = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print a[0, ::2]

a = np.identity(5).astype(int)

b = np.zeros((3,4))

c = np.ones((3,4))
print c

a = np.linspace(0,1,num=10)
print a

x = np.linspace(0,1,num = 5)
y = np.linspace(0,1,num = 5)

xx,yy = np.meshgrid(x,y)

print (xx, yy)

from PIL import Image

Im = Image.open('frutas.jpg')
print(Im.format, Im.size, Im.mode)
Im.show()
Im_g = Im.convert('L')
print(Im_g.format, Im_g.size, Im_g.mode)
Im_g.show()
Im_g.save('fruta_gris.jpg')

from PIL import Image
import matplotlib.pyplot as plt

Im_a = np.array(Image.open('frutas.jpg'))
print(Im_a.shape, Im_a.dtype)
plt.imshow(Im_a)

Im_g = Image.open('frutas.jpg').convert('L')
Im_ga = np.array(Im_g)
print(Im_ga.shape, Im_ga.dtype)
plt.figure()
plt.gray()
plt.imshow(Im_ga)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Im_a = np.array(Image.open('frutas.jpg'))
print(Im_a.shape, Im_a.dtype)
plt.imshow(Im_a)

Im_R = Im_a[:,:,0]
Im_G = Im_a[:,:,1]
Im_B = Im_a[:,:,2]

print(Im_R.shape, Im_R.dtype)
plt.figure()
plt.gray()
plt.imshow(Im_R)

plt.figure()
plt.gray()
plt.imshow(Im_G)

plt.figure()
plt.gray()
plt.imshow(Im_B)

K = 9
M = 15
i = K
suma = 0

if K < M and M > K:   
    print('Correcto')

for i in range(M + 1):
    print i

    
while i < M:
    print (i)
    i += 2
    
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Im_g = Image.open('img1.jpg').convert('L')
Im_ga = np.array(Im_g)
print(Im_ga.shape, Im_ga.dtype)
Im2 = 255 - Im_ga
#plt.gray()
plt.imshow(Im_ga)

plt.figure()
#plt.gray()
plt.imshow(Im2)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.double(np.array(Im_g))
Im2 = np.log(1+Im_ga)
Im2 = np.uint8(255*Im2/Im2.max())
plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.figure()
plt.gray()
plt.imshow(Im2)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import my_linealT as trans

Im_g = Image.open('img1.jpg').convert('L')
Im_ga = np.array(Im_g)
Im2 = trans.my_gamma(Im_ga, 2)
plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.figure()
plt.gray()
plt.imshow(Im2)

from PIL import Image, ImageFilter
 
foto = Image.open('fruit.jpg').convert('L')
 
#Laplace
coeficientes = [1, 1, 1, 1, -8, 1, 1, 1, 1]
datos_laplace = foto.filter(ImageFilter.Kernel((3,3), coeficientes, 1)).getdata()
#datos de la imagen
datos_imagen = foto.getdata()
 
#factor de escalado
w = 1 / 3
 
#datos de imagen menos datos de Laplace escalados
datos_nitidez = [datos_imagen[x] - (w * datos_laplace[x]) for x in range(len(datos_laplace))]
 
imagen_nitidez = Image.new('L', foto.size)
imagen_nitidez.putdata(datos_nitidez)
imagen_nitidez.save('fruitExample.jpg')
 
foto.close()
imagen_nitidez.close()


from PIL import Image

A = 120
B = 135

foto=Image.open('fruit.jpg')

#si la imagen no es a escala de grises se hace la conversion
if foto.mode != 'L':
    foto=foto.convert('L')

#el umbral esta forzosamente comprendido entre 1 y 254 para las
#imagenes de 8 bits a escala de grises
#umbral=65

datos=foto.getdata()
datos_binarios=[]

for B in datos:
    if B<A:
        datos_binarios.append(1)
        continue
    #si es mayor o igual a umbral se agrega 1 en ves de 0
    #podria hacerse con 255 en ves de 1
    datos_binarios.append(0)
    
#en caso de utilizar 255 como valor superior el metodo new
#llevaria 'L' en ves de '1' en el primer argumento
nueva_imagen=Image.new('1', foto.size)
nueva_imagen.putdata(datos_binarios)
nueva_imagen.save('fruitExample120135.jpg')

nueva_imagen.close()
foto.close()

import numpy as npx
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import my_linealT as trans

Im_g = Image.open('img1.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)

h = trans.my_hist(Im_ga)
plt.figure()
plt.bar(np.arange(256),h)

Im_eq = trans.my_equal(Im_ga,h)
plt.figure()
plt.gray()
plt.imshow(Im_eq)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Computer Vision Repository')
import my_linealT as trans


Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.array(Im_g)
Im2 = trans.my_gamma(Im_ga, 0.05)
plt.gray()
plt.imshow(np.uint8(Im_ga))
plt.figure()
plt.gray()
Im = Image.fromarray(Im2)
plt.imshow(Im2)
    
x = np.array[(0.05, 0.10, 0.20, 0.50, 1, 1.5, 2.5, 5.0, 10.0, 25.0)]

for i in x:
    A = i[0]
    Im_g = Image.open('img2.jpg').convert('L')
    Im_ga = np.array(Im_g)
    imageList = trans.my_gamma(Im_ga, A)
    imageResponse = Image.new('1', Im_ga.size)
    imageResponse.putdata(imageList)
    plt.figure()
    plt.gray()
    plt.imshow(imageResponse)

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

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

Im = Image.open('fruit.jpg')
plt.figure()
plt.gray()
plt.imshow(Im)

image = Image.open('fruit.jpg').convert('L')
imagePrint = np.array(image)
plt.figure()
plt.imshow(imagePrint)
imageView = fun.negative(image)
plt.figure()
plt.imshow(imageView)

x = np.array([0.5, 3])

Im_g = Image.open('fruit.jpg').convert('L')

for i in x:
    A = i    
    Im_ga = np.array(Im_g)
    imageList = fun.my_gamma(Im_ga, A)
    
    plt.figure()
    plt.gray()
    plt.imshow(imageList)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

Im_g = Image.open('muchaLuz.jpg').convert('L')
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

r = input("introduce el valor de r: ")
s = input("introduce el valor de s: ")

i = 0
acum = 0

while i < s:    
    i += 1
    suma = r ** i     
    acum = acum + suma
acumResult = acum + 1
print("El valor hallado es: " + str(acumResult))
    
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

Im_g = Image.open('opaca.jpg').convert('L')
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

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters

Im_g = Image.open('img3.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)

Im_f1 = filters.uniform_filter(Im_ga,3)
plt.figure()
plt.gray()
plt.imshow(Im_f1)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters

Im_g = Image.open('img3.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)

Im_f1 = filters.gaussian_filter(Im_ga,3)
plt.figure()
plt.gray()
plt.imshow(Im_f1)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters
import funciones as fun

Im_g = Image.open('noise2.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)

[row, col] = Im_ga.shape;
Im_n = np.double(Im_ga)
for i in range(0,row-1):
    for j in range (0,col-1):
        Im_n[i,j] = Im_n[i,j]+np.random.uniform(0,100)

plt.figure()
plt.gray()
plt.imshow(Im_n)
plt.title("Imagen con ruido")

Im_f1 = filters.gaussian_filter(Im_n,0.7)
plt.figure()
plt.gray()
plt.imshow(Im_f1) 
plt.title("Filtro Gaussiano")

#para corroborar que el mse esta bien se le envia 2 veces la misma
#imagen y debe devolver 0 

print (fun.my_mse(Im_f1, Im_n))

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

Im_g = Image.open('building.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.title("Imagen en esacala de grises")

[Ig, Ix, Iy] = fun.my_gradient(Im_ga)
plt.figure()
plt.gray()
plt.imshow(Ix) 
plt.title("Derivada en x")

plt.figure()
plt.gray()
plt.imshow(Iy) 
plt.title("Derivada en y")

plt.figure()
plt.gray()
plt.imshow(Ig) 
plt.title("Gradiente")    
    
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Im_g = Image.open('building.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga, cmap='hot')
plt.title("Imagen con color falso")

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun

Im = Image.open('build.jpg')
Im_a = np.array(Im)
Im_cmy = fun.my_rgb2cmy(Im_a)
Im_rgb = fun.my_cmy2rgb(Im_cmy)

plt.subplot(131)
plt.imshow(Im_a)
plt.axis("off")
plt.subplot(132)
plt.imshow(Im_cmy)
plt.axis("off")
plt.subplot(133)
plt.imshow(Im_rgb)
plt.axis("off")

plt.figure()

plt.subplot(231)
plt.imshow(Im_a[:,:,0],cmap='gray')
plt.axis("off")
plt.subplot(232)
plt.imshow(Im_a[:,:,1],cmap='gray')
plt.axis("off")
plt.subplot(233)
plt.imshow(Im_a[:,:,2],cmap='gray')
plt.axis("off")

plt.subplot(234)
plt.imshow(Im_cmy[:,:,0],cmap='gray')
plt.axis("off")
plt.subplot(235)
plt.imshow(Im_cmy[:,:,1],cmap='gray')
plt.axis("off")
plt.subplot(236)
plt.imshow(Im_cmy[:,:,2],cmap='gray')
plt.axis("off")

from PIL import Image
import matplotlib.pyplot as plt

Im = Image.open('coins.jpg').convert('L')

umbral=160

datos=Im.getdata()
datos_binarios=[]

for x in datos:
    if x < umbral:
        datos_binarios.append(1)
        continue
    datos_binarios.append(0)

ibn=Image.new('1', Im.size)
ibn.putdata(datos_binarios)
plt.figure()
plt.gray()
plt.imshow(ibn) 
plt.title("Negro y Blanco")   

from PIL import Image
import matplotlib.pyplot as plt
import funciones as fun
import numpy as np

Im = Image.open('coins.jpg').convert('L')
image = np.array(Im)

umbral=160

ImTH = fun.my_threshold(Im,umbral)

plt.gray()
plt.imshow(ImTH) 
plt.title("Negro y Blanco")   

from PIL import Image
import matplotlib.pyplot as plt
#import funciones as fun
import numpy as np

Im = Image.open('building.jpg')
Im_a = np.array(Im)
plt.imshow(Im_a)

[row, col, nb] = Im_a.shape
Im_n = np.zeros(Im_a.shape)
Im_n = Im_a+125*np.random.rand(row,col,nb)
Im_n = np.uint8(255*Im_n/Im_n.max())
plt.figure()
plt.imshow(Im_n)

import funciones as fun

[H, S, I] = fun.rgb2hsi((10),(20),(30))
print ("valor de H: " + str(H))
print ("valor de S: " + str(S))
print ("valor de I: " + str(I))

[R, G, B] = fun.hsi2rgb(210,50,20)
print ("valor de R: " + str(R))
print ("valor de G: " + str(G))
print ("valor de B: " + str(B))

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import funciones as fun

Im = Image.open('build.jpg')
Im_a = np.array(Im)
plt.figure()
plt.imshow(Im_a)
plt.title('IMAGEN ORIGINAL')

Im_cmy = fun.my_rgb2cmy(Im_a)
plt.figure()
plt.imshow(Im_cmy)
plt.title('IMAGEN  CMY')

Im_double = np.double(Im_a) 
[row, col, nb] = Im_double.shape

[H,S,I] = fun.rgb2hsi(row/255, col/255, nb/255)
print ("valor de H: " + str(H))
print ("valor de S: " + str(S))
print ("valor de I: " + str(I))

#Im_rgb = fun.my_cmy2rgb(Im_cmy)
#plt.figure()
#plt.imshow(Im_rgb)
#plt.title('IMAGEN  RGB')
#plt.axis("off")
#
#Im_hsi = fun.rgb2hsi(Im_rgb)
#plt.figure()
#plt.imshow(Im_hsi)
#plt.title('IMAGEN  HSI')
#plt.axis("off")
"""




