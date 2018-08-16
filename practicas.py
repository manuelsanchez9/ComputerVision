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
"""

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





    
 









