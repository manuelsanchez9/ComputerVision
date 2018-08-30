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
"""






