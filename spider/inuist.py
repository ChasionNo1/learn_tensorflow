# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/8/3 8:41
# @Author    :   Chasion
# Description:
import requests


url = 'http://10.255.255.34/authentication/detail'

headers = {
'Host': '10.255.255.34',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
print(response.text)