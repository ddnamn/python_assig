# import module
import cv2
from matplotlib import pyplot as plt 
import numpy as np 
# proccess
image = cv2.imread('gambar.png')
image_shape = np.zeros(image.shape,np.uint8)
image_shape[:,:,1] = image[:,:,1]
image_shape[:,:,2] = image[:,:,2]
image_shape[:,:,0] = image[:,:,0]
result=cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
# show result
plt.figure()
plt.imshow(result)
plt.title('result')
plt.show()