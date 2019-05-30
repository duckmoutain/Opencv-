# -*- coding: utf-8 -*-
import cv2

capture = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #获取轮廓
    gray1 = cv2.Canny(frame, 300, 200)

    cv2.imshow('frame', frame)
    cv2.imshow('frame2',  gray)
    cv2.imshow('frame3', gray1)
    #print(gray)
    #cv2.waitKey()
    if cv2.waitKey(1) == ord('q'):
      break
