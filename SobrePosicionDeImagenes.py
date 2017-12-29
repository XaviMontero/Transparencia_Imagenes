# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:36:44 2017

@author: asus
"""

import cv2
import numpy as np

# Load two images
img1 = cv2.imread('3D-Matplotlib.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('mainlogo.png') 
img3 = cv2.imread('cap1.PNG') 
rows,col,channels = img2.shape
rows1,col1,channels1 = img3.shape
cv2.imshow('original',img2)
cv2.imshow('original1',img3)
roi = img1[0:rows,0:col]
roi1= img1[0:rows1,200:col1+200]
img2Gray= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img3Gray= cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2Gray, 220,255,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
dst =cv2.add(img1_bg,img2_fg)
ret1, mask1 = cv2.threshold(img3Gray, 0,255,cv2.THRESH_BINARY)
mask_inv1=cv2.bitwise_not(mask1)
img11_bg=cv2.bitwise_and(roi1,roi1,mask=mask_inv1)
img22_fg=cv2.bitwise_and(img3,img3,mask=mask1)
dst1 =cv2.add(img11_bg,img22_fg)
img1[0:rows,0:col]=dst
img1[0:rows1,200:col1+200]=dst1
cv2.imshow('result',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()