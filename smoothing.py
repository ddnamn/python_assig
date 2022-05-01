# import library 
import numpy as np 
from matplotlib import pyplot as plt 
import cv2 
# import image
image = cv2.imread('cat.png')
# sharpening
def bKernel(size):
    k = np.ones((size,size),np.float32)/(size**2)
    return k 
result=cv2.filter2D(image,-1,bKernel(5))

# show the result 
cv2.imshow("Original Image", image)
plt.title('result')
plt.subplot(1,1,1)
plt.imshow(result)
plt.show()