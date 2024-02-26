import cv2
import numpy as np 
img=cv2.imread('ansheet2.jpg')
#img=cv2.pyrDown(img)
#img=cv2.pyrDown(img)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_binary=img_thre=cv2.adaptiveThreshold(img_gray,100,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,30)

cv2.imshow('test',img_binary)
cv2.waitKey(0)

kernel=np.ones((3,3),np.uint8)
#img_open=cv2.morphologyEx(img_binary,cv2.MORPH_OPEN,kernel)
img_open=(cv2.dilate(img_binary,kernel,iterations=3))
img_open=(cv2.erode(img_open,kernel,iterations=3))

contours,hierarchy=cv2.findContours(img_open,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#img_open=cv2.bitwise_not(img_open)

locations=[]
for cnt in contours:
    x,y,w,h=cv2.boundingRect(cnt)
    if w>h and w<100 and h<100:
        cv2.rectangle(img_open,(x,y),(x+w,y+h),(0,0,255),1)
        locations.append((x,y))

print(locations)
cv2.imshow('img',img_open)
cv2.waitKey(0)
