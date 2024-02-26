import cv2
import numpy as np 
img=cv2.imread('test.jpg')
img=cv2.pyrDown(img)
img=cv2.pyrDown(img)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_binary=img_thre=cv2.adaptiveThreshold(img_gray,100,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,30)

kernel=np.ones((3,3),np.uint8)
#img_open=cv2.morphologyEx(img_binary,cv2.MORPH_OPEN,kernel)
img_open=(cv2.dilate(img_binary,kernel,iterations=3))
img_open=(cv2.erode(img_open,kernel,iterations=3))

contours,hierarchy=cv2.findContours(img_open,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#img_open=cv2.bitwise_not(img_open)

xx=[]
yy=[]
for cnt in contours:
    x,y,w,h=cv2.boundingRect(cnt)
    cv2.rectangle(img_open,(x,y),(x+w,y+h),(0,0,255),1)
    xx.insert(-1,x)
    yy.insert(-1,y)


leftup=[1000000000000000000000,-1]
for i in range(0,len(xx)):
    leftup2 = [(xx[i]) ** 2+(yy[i] )**2,(xx[i],yy[i])]
    if leftup2[0]<leftup[0]:
        leftup=leftup2


rightdown=[0,-1]
for i in range(0,len(xx)):
    rightdown2 = [(xx[i]) ** 2+(yy[i] )**2,(xx[i],yy[i])]
    if rightdown2[0]>rightdown[0]:
        rightdown=rightdown2


x1,y1=list(leftup[1])

x2,y2=list(rightdown[1])

img_open=img_open[x1:x2,y1:y2]

cv2.imshow('img1',img_open)
cv2.waitKey(0)