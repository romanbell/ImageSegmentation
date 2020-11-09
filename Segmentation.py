from skimage.color import rgb2gray
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline   #Only works in Jupiter 
from scipy import ndimage

image = plt.imread('car.jpg')
image.shape
plt.imshow(image)
plt.show()

gray = rgb2gray(image)
plt.imshow(gray, cmap='gray')
plt.show()

gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray, cmap='gray')
#plt.show()
