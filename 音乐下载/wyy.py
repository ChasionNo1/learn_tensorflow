"""
文件说明

"""
import requests
import json
import os


def search(search_name):
    data = {'types': 'search',
            'count': '20',
            'source': 'netease',
            'pages': '1',
            'name': search_name}
    response = requests.post(url=url, data=data)
    # 替换非法字符，方式编码错误
    info_str = response.text.replace('/', '\\')
    rec_str = info_str.encode('utf-8').decode("unicode_escape")
    # 对修改后的字符进行提取，
    first_index = rec_str.find('(')
    info = rec_str[first_index + 1:-1]
    # print(type(info))
    # print(info)
    # 字符串转为list
    info_list = eval(info)
    # print(info_list[1])
    list_length = len(info_list)

    for i in range(list_length):
        result_dict['order'] = i + 1
        result_dict['name'] = info_list[i]['name']
        result_dict['artist'] = info_list[i]['artist']
        result_dict['album'] = info_list[i]['album']
        result_dict['id'] = info_list[i]['id']
        result_list.append(result_dict.copy())

    for j in range(len(result_list)):
        print(result_list[j])


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


# 传入要下载的歌曲序号
def download_music(index):

    down_data = {'types': 'url',
                 'id': result_list[index-1]['id'],
                 'source': 'netease'}
    down_info = requests.post(url=url, data=down_data)
    # print(down_info.text)
    a = down_info.text.find('(')
    url_str = down_info.text[a+1:-1]
    url_dict = json.loads(url_str)
    real_url = url_dict['url']
    if len(real_url) > 10:
        download = requests.get(real_url)
        music_name = str(result_list[index - 1]['artist'][0]) + ' - ' + str(result_list[index - 1]['name'])
        mkdir(r'E:\MUSIC\wy')
        with open(r'E:\MUSIC\wy\{0}.mp3'.format(music_name), 'wb') as f:
            f.write(download.content)
            print('下载完成')
    else:
        print('没有资源')


if __name__ == '__main__':
    url = 'http://y.webzcz.cn/api.php?callback=jQuery111309803561823397193_1597587452727'
    # 创建两个集合，list dict
    result_list = []
    result_dict = {}
    while 1:
        print("输入搜索内容：")
        search(input())
        print("输入下载编号：")
        download_music(int(input()))

