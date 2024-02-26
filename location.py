import requests
import base64
import json

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
# 二进制方式打开图片文件
f = open('test4.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.ba5ab4b78a22641b0574d71ec9f51722.2592000.1709282168.282335-48885010'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print ('response')

dict11=response.json()
list11=dict11['words_result']
for i in range(1,len(list11)):
    dict12=list11[i]
    str=dict12['words']
    if str.find('1')!=-1:
        print(str,dict12['location'],sep=':')