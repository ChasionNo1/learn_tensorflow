"""
文件说明
获取基金的实时估值
"""
import requests
import json
from decimal import Decimal


def deal_jijin_info(code):
    url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183041039934333233385_1597280775462&fundCode=' + code +'&pageIndex=1&pageSize=20&startDate=&endDate=&_=1597280775479'
    headers = {'Host': 'api.fund.eastmoney.com',
               'Referer': 'http://fundf10.eastmoney.com/jjjz_' + code + '.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    info_str_index = response.text.find('(')
    # 将字符串转化为字典处理
    rec_dict = json.loads(response.text[info_str_index + 1:-1])
    # print(rec_dict)
    # 提取详细信息
    # print(rec_dict['Data']['LSJZList'])
    # 20天的基金净值
    total = Decimal('0.00')
    loop_number = len(rec_dict['Data']['LSJZList'])
    for i in range(7):
        draw_dict['时间'] = rec_dict['Data']['LSJZList'][i]['FSRQ']
        draw_dict['单位净值'] = rec_dict['Data']['LSJZList'][i]['DWJZ']
        if rec_dict['Data']['LSJZList'][i]['JZZZL'] != '':
            draw_dict['日增长率'] = rec_dict['Data']['LSJZList'][i]['JZZZL']
            a = Decimal(rec_dict['Data']['LSJZList'][i]['JZZZL'])
            total = a + total
        else:
            draw_dict['日增长率'] = '未公布'
        draw_list.append(draw_dict.copy())
    # print(draw_list)
    return draw_list


def deal_real_time_data(code):
    # http://fundgz.1234567.com.cn/js/001595.js?rt=1597298689396
    url = 'http://fundgz.1234567.com.cn/js/' + code + '.js?rt=1599125136782'
    response = requests.get(url)
    real_time_info_index = response.text.find('(')
    real_time_info = response.text[real_time_info_index + 1:-2]
    info_dict = json.loads(real_time_info)
    # print(real_time_info)
    real_time_dict['基金名称'] = info_dict['name']
    real_time_dict['单位净值'] = info_dict['dwjz']
    real_time_dict['估算净值'] = info_dict['gsz']
    real_time_dict['估算增长率'] = info_dict['gszzl']
    real_time_dict['估算时间'] = info_dict['gztime']
    real_time_dict['操作建议'] = '无操作'
    print(real_time_dict)
    # 这里调用了jijin里函数得到七日数据
    info_list = deal_jijin_info(code)
    # 这里进行操作建议，得到前三日的情况，再根据今日情况
    '''
    
    '''
    # 例如：前三日已经大跌，今日还是大跌，可以建仓或者加仓，或者前三日大涨，今日还是大涨，进行提醒
    two_day_sum = Decimal(0.0)
    # print(info_list[0])
    print(real_time_list)
    for i in range(2):
        two_day_sum = two_day_sum + Decimal(info_list[i]['日增长率'])
    three_day_sum = two_day_sum + Decimal(info_list[2]['日增长率'])
    if Decimal(info_list[0]['日增长率']) < -2 and Decimal(real_time_dict['估算增长率']) < -1:
        real_time_dict['操作建议'] = '昨日大跌' + str(info_list[0]['日增长率']) + '今日大跌'
    if two_day_sum < -3 and Decimal(real_time_dict['估算增长率']) < 0:
        real_time_dict['操作建议'] = '前两日大跌' + str(two_day_sum) + '今日负增长'
    if three_day_sum > 4:
        real_time_dict['操作建议'] = '近日大幅增长'
    real_time_list.append(real_time_dict.copy())
    # print(real_time_list)
    with open('jjrecord.txt', 'a') as f:
        f.write(str(real_time_list[0]) + '\r\n')


def print_list(input_list, code):
    deal_real_time_data(code)
    # 控制打印输出的格式对齐
    # 因为汉字比空格胖一些，所以还需要进一步调整
    name_length = len(input_list[0]['基金名称'])
    if name_length < 8:
        space_number = 17 - name_length
    elif name_length > 9:
        space_number = 14 - name_length
    else:
        space_number = 16 - name_length
    print('| 基金名称              单位净值          估算净值           估算增长率        估算时间                   操作提示')
    print('| '+input_list[0]['基金名称']+' '*space_number + input_list[0]['单位净值']+'           '+input_list[0]['估算净值']+'             '+input_list[0]['估算增长率']+'          '+input_list[0]['估算时间']+'          '+input_list[0]['操作建议'])


if __name__ == '__main__':
    d = 0
    # 从文件中加载基金代码和名称
    jj_name = []
    jj_code = []
    with open('jjname.txt', 'r', encoding='UTF-8', buffering=True) as g:
        while True:
            line = g.readline()
            if not line: break
            line = line.strip('\n')
            if d == 0:
                jj_name.append(line)
                d = d + 1
            else:
                jj_code.append(line)
                d = d - 1
    print('-------------------------------------基金估值情况---------------------------------------------')
    for k in range(len(jj_code)):
        real_time_list = []
        real_time_dict = {}
        draw_list = []
        draw_dict = {}
        print_list(real_time_list, jj_code[k])
        print('---------------------------------------------------------------------------------------------')

