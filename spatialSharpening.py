# # import library yang dibutuhkan
import cv2 as cv 
import numpy as np 
# ambil gambar
img= cv.imread('kucing.jfif')
# sharp prosess
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])
img_sharp = cv.filter2D(img, -1, kernel)

# inisial dan tampilkan hasil
cv.imshow('output', img_sharp)
cv.waitKey(0)