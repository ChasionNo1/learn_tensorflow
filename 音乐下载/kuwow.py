import requests
import urllib.parse
import os


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def search(name):
    search_name = name
    search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&reqId=24b2acb0-e1f4-11e9-9c10-df22c38d9fb9'.format(urllib.parse.quote(search_name))
    headers = {'Cookie': 'Cookie: _ga=GA1.2.1209502700.1578305434; _gid=GA1.2.570101734.1578305434; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1578305434; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1578305434; kw_token=EQ4EIPN5TE7',
               'Host': 'www.kuwo.cn',
               'csrf': 'EQ4EIPN5TE7',
               'Referer': 'http://www.kuwo.cn/search/list?key=%E8%AE%B8%E5%B5%A9',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    response = requests.get(url=search_url, headers=headers)
    rec = response.json()
    '''
    得到歌曲信息 name id
    '''
    music_info = []
    music = {}
    for i in range(len(rec['data']['list'])):
        music['排序'] = i + 1
        music['name'] = rec['data']['list'][i]['name']
        music['id'] = rec['data']['list'][i]['rid']
        music['singer'] = rec['data']['list'][i]['artist']
        music_info.append(music.copy())
        print(music)
    
    print('选择要下载的编号，多个序号以中文逗号间隔:')
    download_number = input()
    # 中文逗号间隔
    index = download_number.split('，')
    for i in range(len(index)):
        file_name = str(music_info[int(index[i])-1]['singer']) + ' - ' + str(music_info[int(index[i])-1]['name'])
        download(music_info[int(index[i])-1]['id'], file_name)

# 这里给download函数传入下载的即可，至于命名


def download(id, name):
    file_name = name
    download_id = id
    info_url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=320kmp3&from=web&t=1569668134762&reqId=717bbfe5-a891-49c2-b549-c923ea781cec'.format(download_id)
    headers2 = {'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1569666496,1569668107; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1569677402',
                'Host': 'www.kuwo.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    getaddr = requests.get(url=info_url, headers=headers2)
    realurl = getaddr.json()
    url = realurl['url']
    # print(url)
    download = requests.get(url=url)
    mkdir(r'E:\MUSIC\kuwo')
    with open(r'E:\MUSIC\kuwo\{0}.mp3'.format(file_name), 'wb') as f:
        f.write(download.content)
    print('{}   下载完成!'.format(file_name))


if __name__ == '__main__':
    while 1:
        name = input('输入搜索内容：')
        search(name)

