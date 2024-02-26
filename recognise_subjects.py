import requests
import base64
import json

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('English2.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.ba5ab4b78a22641b0574d71ec9f51722.2592000.1709282168.282335-48885010'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print('response')

dict1=response.json()
list1=dict1['words_result']
for i in range(1,len(list1)):
    dict2=list1[i]
    str=dict2['words']
    subjects=['语文','数学','英语','物理','化学','生物','政治','历史','地理']
    for subject in subjects:
        if str.find(subject)!= -1:
            print(subject)
