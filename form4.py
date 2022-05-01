# import library 
import cv2
import numpy as np
# ambil gambar 
img1 = cv2.imread('gambar.png')
img2 = cv2.imread("gambar2.png")
# metode and or xor 
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
# tampilkan gambar
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize image 
# img1 = cv2.resize(img1, (400,300))
# img2 = cv2.resize(img2, (400,300))

# cv2.imshow('bitNot1', bitNot1)
# cv2.imshow('bitNot2', bitNot2)
# bitNot1 = cv2.bitwise_not(img1)
# bitNot2 = cv2.bitwise_not(img2)