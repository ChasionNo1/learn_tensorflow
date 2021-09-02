# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/8/23 10:07
# @Author    :   Chasion
# Description:
import cv2


src = cv2.imread('001.png')
cv2.imshow('src', src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.imwrite('002.png', gray)
cv2.waitKey()