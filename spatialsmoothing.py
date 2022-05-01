# import library yang dibutuhkan
import cv2
import numpy as np
from matplotlib import pyplot as plt
# load gambar
img = cv2.imread('kucing.jfif')
# ubah warna gambar dari bgr ke rgb
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# definisi kernel
kernel = np.ones((5,5),np.float32)/25
# destinasi gambar
dst=cv2.filter2D(img,-1,kernel)
# inistial result
titles = ['IMAGE','SMOOTHING SPATIAL']
images=[img,dst]
# smoothing process
for i in range (2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# tampilkan hasil
plt.show()