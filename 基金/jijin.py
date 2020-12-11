"""
文件说明
用来计算估值与实际值的误差，以及一些基金详情
实现功能：
1、查看最近的净值波动情况
2、计算估值与实际值的误差
3、计算近20日的总增长

2020-8-20更新：
1、更改为7日汇总
2、添加操作建议代码（根据前三日的变动和前一日大幅度变动给出操作建议）
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
    return total, draw_list


# 整体的思路是，计算前三日的增长总和，对于债券如果三日总和在-0.5到-1之间，需要进行加仓，其他不需要
# 对于其他高风险的基金，前三日负增长总和小于-3则需要关注（在当日15：00之前操作），连续正增长4日且总和大于5以上则需要适当减仓
# def operation_suggestions():
#     # 计算前三日的顺序，先近后远
#     three_day_sum = Decimal(0.0)
#     for i in range(3):
#         three_day_sum = three_day_sum + Decimal(draw_list[i]['日增长率'])
#     if three_day_sum < -3:
#         print('当日15：00之前操作,建仓或加仓')
#     if three_day_sum > 4:
#         print('近日大幅增长')


def print_list(input_list, jj_code):
    total, _ = deal_jijin_info(jj_code)
    print('    时间          单位净值          日增长率          近7日总增长')
    for j in range(7):
        if j == 0:
            print(input_list[j]['时间'] + '        ' + input_list[j]['单位净值'] + '           ' + input_list[j]['日增长率'] + '           ' + str(total))
        else:
            print(input_list[j]['时间'] + '        ' + input_list[j]['单位净值'] + '           ' + input_list[j]['日增长率'])


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
    for k in range(len(jj_code)):
        draw_list = []
        draw_dict = {}
        print('--------------------------------------------')
        print(jj_name[k])
        print_list(draw_list, jj_code[k])
        # operation_suggestions()


