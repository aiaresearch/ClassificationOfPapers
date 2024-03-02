from sklearn.cluster import KMeans
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
locations=[]
for cnt in contours:
    x,y,w,h=cv2.boundingRect(cnt)
    if w>h and w<100 and h<100:
        cv2.rectangle(img_open,(x,y),(x+w,y+h),(0,0,255),1)
        locations.append((x,y))
        xx.append(x)
        yy.append(y)


y=km_model = KMeans(n_clusters=3,n_init=10,init='random').fit_predict(locations)

top=100000000000
new=[]
for i in range(0,len(y+1)):
    new.append([locations[i],y[i]])
    if y[i]==1:
        str='1'
    else:
        str='2'
        if xx[i]<top:
            top=xx[i]
    cv2.putText(img_open,str,locations[i],1,1,(255,0,0))
print(top)
#img_open=img_open[0:top,:]
cv2.imshow('img',img_open)
cv2.waitKey(0)


