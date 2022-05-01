# import library opencv yg dibutuhkan
import cv2
import numpy as np
import matplotlib.pyplot as plt
# membaca input gambar
img =cv2.imread('gambar.png',0)
# cari frquensi pixel dari range 0-255
plt.hist(img.ravel(),256,[0,256])
# tampil garfik ploting histogram dari gambar 
plt.show()