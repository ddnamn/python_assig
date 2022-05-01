# import library 
import cv2  
import numpy as np 
# import image 
image = cv2.imread('kucing.jfif')
# change RGB to CMYK
img = image.astype(np.float64)/255.
K = 1 - np.max(img, axis=2)
C = (1-img[...,2] - K)/(1-K)
M = (1-img[...,1] - K)/(1-K)
Y = (1-img[...,0] - K)/(1-K)
CMYK_image= (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
# show the result
cv2.imshow("Original Image", image)
cv2.imshow("CMYK Image", CMYK_image)
cv2.waitKey(0)
cv2.destroyAllWindows()