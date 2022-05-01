# import library yang dibutuhkan 
import numpy
import cv2 as cv

# ambil gambar
gmbr = cv.imread('image.jfif',0)
# ubah ke histogramEqualisation 
eq=cv.equalizeHist(gmbr)
# tampilkan hasil 
cv.imshow('output',eq)
cv.waitKey(0)
cv.destroyAllWindows()