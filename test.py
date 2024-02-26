import cv2 

img=cv2.imread('test.jpg')
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(g,500,0.1,10)
xx=[]
yy=[]
for corner in corners:
    x,y=corner.ravel()
    xx.insert(-1,x)
    yy.insert(-1,y)
print(max(xx))
print(max(yy))