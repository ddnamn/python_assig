import numpy as np
import cv2
# Load the image
img = cv2.imread('image.jfif')
# Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
gamma_two_point_two = np.array(255*(img/255)**2.2,dtype='uint8')
# Similarly, Apply Gamma=0.4 
gamma_point_four = np.array(255*(img/255)**0.4,dtype='uint8')
# Display the images in subplots
img3 = cv2.hconcat([gamma_two_point_two,gamma_point_four])
cv2.imshow('a2',img3)
cv2.waitKey(0)