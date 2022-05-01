import numpy as np
import cv2

def  main():
    img1 = cv2.imread('gambar.png')
    img2 = cv2.imread('gambar2.png')
  
    diffImg1 = cv2.subtract(img1,img2)  
    diffImg2 = cv2.subtract(img2, img1)
    diffImg3 = img1 - img2
    diffImg4 =  img2 - img1

    cv2.imshow('subtract(img1,img2)',diffImg1)
    cv2.imshow('subtract(img2,img1)', diffImg2)
    cv2.imshow('img1 - img2',diffImg3)
    cv2.imshow('img2 - img1', diffImg4)

    cv2.waitKey(0)

main()