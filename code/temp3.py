from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import my_linealT as trans 

Im_g = Image.open('P12bb.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

h = trans.my_hist(Im_ga)
plt.figure()
plt.bar(np.arange(256),h)

Im_eq = trans.my_equal(Im_ga,h)
plt.figure()
plt.gray()
plt.imshow(Im_eq)
plt.axis("off")

h2 = trans.my_hist(Im_eq)
plt.figure()
plt.bar(np.arange(256),h2)





