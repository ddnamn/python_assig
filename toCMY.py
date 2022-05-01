# import library 
import cv2
import numpy as np 

# import image
img=cv2.imread('cat.png')
# inisialtize height , width , and channels 
height =  img.shape[0]
width  =img.shape[1]
channels  =img.shape[2]
# 
cmy = np.zeros((height,width, 3))

for x in np.arange(height):
    for z in np.arange(width):
        r = img.item (x,z,0)
        g = img.item (x,z,1)
        b= img.item (x,z,2)

        c = 1 - r/255
        m = 1 - g/255
        y = 1 - b/255

        cmy.itemset((x,z,0), c)
        cmy.itemset((x,z,1), m)
        cmy.itemset((x,z,2), y)


# show result
cv2.imshow('Output', cmy)
cv2.waitKey(0)
