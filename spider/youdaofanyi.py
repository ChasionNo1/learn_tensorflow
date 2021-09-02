# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/23 15:04
# @Author    :   Chasion
# Description:
import requests
import time
import hashlib
import random
#  , c = p.md5("new-fanyiweb" + l + "ydsecret://newfanyiweb.doctran/sign/0j9n2{3mLSN-$Lg]K4o0N2}" + o);


def translate(ips):
    e = ips
    salt = str(int(time.time()*10000))
    l = str(int(time.time()) * 1000)
    # print(salt)
    i = l + str(int(random.random() * 10))
    # >>> m = hashlib.md5()
    # >>> m.update(b'123')
    # >>> m.hexdigest()
    m = hashlib.md5()
    s = 'fanyideskweb' + e + i + 'Y2FYu%TNSbMCxc3t2u^XT'
    m.update(bytes(s, encoding='utf-8'))
    sign = m.hexdigest()
    # print(sign)
    # b961b039b62d95be6789b935b04bfa2d
    # c00da146dd21f05c8ed944866654087e

    m2 = hashlib.md5()
    m2.update(b'')
    bv = m2.hexdigest()
    # print(bv)

    data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': l,
        'bv': '5b3e307b66a6c075d525ed231dcc8dcd',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1449049146@222.190.109.119; OUTFOX_SEARCH_USER_ID_NCOO=2041318195.2406044; _ntes_nnid=1879daf3847ddcd223225776c3cec78f,1618212053883; _ga=GA1.2.55886037.1626749821; JSESSIONID=aaaKw9fYpfXp65w6oksRx; SESSION_FROM_COOKIE=www.baidu.com; UM_distinctid=17ad2296388bcd-061ded75b62a04-6373264-1fa400-17ad2296389c23; ___rl__test__cookies={}'.format(l),

        'Host': 'fanyi.youdao.com',
        'Origin': 'https: // fanyi.youdao.com',
        'Referer': 'https: // fanyi.youdao.com /',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.124Safari / 537.36'
    }
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    response = requests.post(url=url, data=data, headers=headers)
    info = response.text
    info = eval(info)
    # print(info)
    print(info['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    print('输入要翻译内容：')
    ips = input()
    translate(ips)