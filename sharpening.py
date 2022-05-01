# import library 
from matplotlib import pyplot as plt
import cv2
import numpy as np 
# import gambar 
img = cv2.imread('image.jfif')
k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
filter_img = cv2.filter2D(img, -1, k)
# tampil hasil 
cv2.imshow('original image', img)
plt.imshow(filter_img)
plt.title('result')
plt.show()
