import cv2
import numpy as np 
img=cv2.imread('ansheet.jpg')
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('input image',img)
cv2.imshow('gray image',imgg)
imgg=cv2.bitwise_not(imgg)
binary=cv2.adaptiveThreshold(imgg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)
cv2.namedWindow('result image',cv2.WINDOW_AUTOSIZE)
cv2.imshow('result image',binary)

hline=cv2.getStructuringElement(cv2.MORPH_RECT,((img.shape[1]//16),1),(-1,-1))
vline=cv2.getStructuringElement(cv2.MORPH_RECT,(1,(img.shape[0]//16)),(-1,-1))

dst=cv2.morphologyEx(binary,cv2.MORPH_OPEN,vline)
dst=cv2.bitwise_not(dst)

cv2.imshow('vline image',dst)
cv2.waitKey(0)

