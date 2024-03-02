import requests
import base64
import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
pca.frequency = 50

servo7 = servo.Servo(pca.channels[7])

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

if subject == '英语':
    for i in range(180):
        servo7.angle = i
        time.sleep(0.03)

pca.deinit()