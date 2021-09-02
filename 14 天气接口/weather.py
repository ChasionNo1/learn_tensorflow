# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/20 11:03
# @Author    :   Chasion
# Description:
import requests
import json

"""
101191305:宿豫区
101190106：江浦
"""

url = 'http://aider.meizu.com/app/weather/listWeather?cityIds=101190106'
response = requests.get(url).text
response = eval(response)
print(type(response))
print(response)

