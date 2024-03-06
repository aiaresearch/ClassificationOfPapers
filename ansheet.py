from sklearn.cluster import KMeans
import cv2
import numpy as np
import requests
import base64

import os
os.environ["OMP_NUM_THREADS"] = '1'

#a=int(input('准考证号有几位？'))
b,c=map(int,input('第几位是班级？（两位之间用空格连接）').split())
img=cv2.imread('ansheet.jpg')
img=cv2.pyrDown(img)
#img=cv2.pyrDown(img)
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
    if w>h and w<150 and h<150:
        cv2.rectangle(img_open,(x,y),(x+w,y+h),(0,0,255),1)
        locations.append((x,y))
        xx.append(x)
        yy.append(y)


y=km_model = KMeans(n_clusters=2,n_init=1,init=np.array([[img.shape[1]/2, 0], [img.shape[1]/2, img.shape[0]]])).fit(locations)

labels = y.labels_

#for i, label in enumerate(labels):
#    print("Cluster:", label)


print(xx)
back=0
new=[]
for i in range(0,len(labels)):
    new.append([locations[i],labels[i]])
    if labels[i]==0:
        _str='0'
        if yy[i]>back:
            back=yy[i]
    else:
        _str='1'
        xx.remove(locations[i][0])
    cv2.putText(img_open,_str,locations[i],1,1,(255,0,0))

img_open=img_open[0:back,:]
img=img[0:back,:]
cv2.imwrite('example.jpg',img)

cv2.imshow('img',img_open)
cv2.waitKey()


xx=list(set(xx))
xx.sort()

def baidu_ocr(image_path, recognize_granularity='small'):
    
    access_token = "24.b0c4639aeba94eb2581ad45a3296592a.2592000.1711979054.282335-48885010"
    
    # OCR
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {'access_token': access_token, 'recognize_granularity': recognize_granularity}
    with open(image_path, 'rb') as file:
        image_data = file.read()
    image_base64 = base64.b64encode(image_data).decode()
    data = {'image': image_base64}
    
    # Send OCR request
    response = requests.post(url, headers=headers, params=params, data=data)
    return response


result = baidu_ocr('example.jpg' ,recognize_granularity='small')
print("OCR Result:", result)

dict1=result.json()

print(dict1)

clas=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
where=[[],[],[],[],[],[],[],[],[],[]]
numbers=['0','2','3','4','5','6','7','8','9']
list0=dict1['words_result']
for i in range(0,len(list0)):
    list0_5=list0[i].get('chars')
    for j in range(0,len(list0_5)):
        str_=list0_5[j].get('char')
        for number in numbers:
            if str_.find(number)!= -1:
            #print(number)
                where[int(number)].append(list0_5[j].get('location'))
                for x in xx:
                    if list0_5[j].get('location').get('left') in range(x,x+w//2):
                        cv2.putText(img_open,'here',(list0_5[j].get('location').get('left'),list0_5[j].get('location').get('height')),1,1,(255,0,0))
                        clas[xx.index(x)].append(number)

print(clas)
column=[member for member in clas if len(member)>5]
print(column)
#print(where)

listb=[]
listb0=column[b-1]
for i in range(0,10):
    i=str(i)
    if listb0.count(i)==0:
        listb.append(i)

if listb!=[1]:
    for item in listb:
        if where[int(item)]!=[] and item!='1':
            b=int(item)
else:
    b=1



listc=[]
listc0=column[c-1]
for i in range(0,10):
    i=str(i)
    if listc0.count(i)==0:
        listc.append(i)

if listc!=[1]:
    for item in listc:
        if where[int(item)]!=[] and item!='1':
            c=int(item)
else:
    c=1

print('班级:',b,c,sep='')

