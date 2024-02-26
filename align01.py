#图像校正示例
import cv2
import numpy as np
import math

im= cv2.imread("scanned-form.jpg")
im=cv2.pyrDown(im)
im=cv2.pyrDown(im)
im=cv2.pyrDown(im)

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# cv2.imshow('im',im)

# 模糊
blurred=cv2.GaussianBlur(gray,(5,5),0)
#膨胀
dilate = cv2.dilate(blurred,(3,3))
# 检测边沿
edged =cv2.Canny(dilate, 30, 120) # 滞后阈值、模糊度
cv2.imshow("edged", edged)

# 轮廓检测
cnts , hie = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #只保留该方向的终点坐标

docCnt = None
# 绘制轮廓
im_cnt=cv2.drawContours(im,cnts,-1, (0,0,255),2)
cv2.imshow("im_cnt",im_cnt)

#计算轮廓面积，并排序
if len(cnts) > 0:
    cnts =sorted(cnts,key=cv2.contourArea,#排序依据，根据contourArea函数结果排序
                 reverse=True)
    for c in cnts:
        peri=cv2.arcLength(c,True) #计算轮廓周长
        approx=cv2.approxPolyDP(c,0.02 * peri,True) # 轮廓多边形拟合
        #轮廓为4个点表示找到纸张
        if len(approx) == 4:
            docCnt = approx
            break

print(docCnt)

#用圆圈标记处角点
points = []
for peak in docCnt:
    peak = peak[0]
    # 绘制圆
    cv2.circle(im,tuple(peak),10,(0,0,255),2)
    points.append(peak) #添加到列表
print(points)
cv2.imshow("im_point",im)
"""
# 校正
src = np.float32([points[0],points[1],points[2],points[3]])# 原来逆时针方向四个点
dst = np.float32([[0,0],[0,488],[337,488],[337,0]]) # 对应变换后逆时针方向四个点
m = cv2.getPerspectiveTransform(src,dst)#生成透视变换矩阵
result = cv2.warpPerspective(gray.copy(),m,(337,488)) # 透视变换
"""

# 根据勾股定理计算宽度、高度，再做透视变换
h = int(math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2))#宽度
w = int(math.sqrt((points[2][0] - points[1][0])**2 + (points[2][1] - points[1][1])**2))#高度
print("w:", w, "h:", h)
src = np.float32([points[0],points[1],points[2],points[3]])
dst = np.float32([[0,0], [0,h] , [w, h] , [w,0]])
m = cv2.getPerspectiveTransform(src,dst) #生成透视变换矩阵
result=cv2.warpPerspective(gray.copy(),m,(w,h)) #透视变换


cv2.imshow("result",result) #显示透视变换结果

cv2.waitKey()
cv2.destroyAllWindows()