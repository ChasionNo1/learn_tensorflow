"""
文件说明

"""
import requests
import json
from decimal import Decimal

draw_list = []
draw_dict = {}
url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183041039934333233385_1597280775462&fundCode=001595&pageIndex=1&pageSize=20&startDate=&endDate=&_=1597280775479'
headers = {'Host': 'api.fund.eastmoney.com',
           'Referer': 'http://fundf10.eastmoney.com/jjjz_001595.html',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
response = requests.get(url=url, headers=headers)
info_str_index = response.text.find('(')
# 将字符串转化为字典处理
rec_dict = json.loads(response.text[42:-1])
# print(rec_dict)
# 提取详细信息
# print(rec_dict['Data']['LSJZList'])
# 20天的基金净值,
loop_number = len(rec_dict['Data']['LSJZList'])
total = Decimal('0.00')
for i in range(loop_number):
    draw_dict['时间'] = rec_dict['Data']['LSJZList'][i]['FSRQ']
    draw_dict['单位净值'] = rec_dict['Data']['LSJZList'][i]['DWJZ']
    draw_dict['日增长率'] = rec_dict['Data']['LSJZList'][i]['JZZZL']
    # 计算近20日增长总和，负的-0.32
    a = Decimal(rec_dict['Data']['LSJZList'][i]['JZZZL'])
    total = a + total
    draw_list.append(draw_dict.copy())

# print(draw_list)
print(total)