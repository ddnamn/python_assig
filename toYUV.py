# import library
import cv2
# import image
image = cv2.imread('hero.png')

# convert RGB to YUV
yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

# show result 
cv2.imshow('original image', image)
cv2.imshow('result', yuv)
cv2.waitKey(0)