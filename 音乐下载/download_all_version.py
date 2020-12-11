import requests
import urllib.parse
import os
import time

'''
整体思路是定义一个类，输入下载的个数和搜索内容
'''


class Music:
    def __init__(self, search_name, number, search_url, download_url, headers1, headers2, path):
        self.search_name = search_name
        self.number = number
        self.url = search_url
        self.download_url = download_url
        self.search_headers = headers1
        self.download_headers = headers2
        self.music_info = []
        self.music = {}
        self.path = path

    def search(self):
        self.url = self.url.format(urllib.parse.quote(self.search_name))
        response = requests.get(url=self.url, headers=self.search_headers)
        rec = response.json()
        '''
        得到歌曲信息 name id
        '''
        for i in range(len(rec['data']['list'])):
            self.music['排序'] = i + 1
            self.music['name'] = rec['data']['list'][i]['name']
            self.music['id'] = rec['data']['list'][i]['rid']
            self.music['singer'] = rec['data']['list'][i]['artist']
            self.music_info.append(self.music.copy())
            print(self.music)

    def download(self):
        for i in range(self.number):
            file_name = str(self.music_info[i]['singer']) + ' - ' + str(
                self.music_info[i]['name'])
            # download(music_info[int(index[i]) - 1]['id'], file_name)
            info_url = self.download_url.format(format(self.music_info[i]['id']))
            get_download_url = requests.get(url=info_url, headers=self.download_headers)
            download_url = get_download_url.json()['url']
            time.sleep(1)
            download_music = requests.get(url=download_url)
            self.mkdir()
            with open(r'D:\MUSIC\kuwo\{0}.mp3'.format(file_name), 'wb') as f:
                f.write(download_music.content)
            print('{}   下载完成!'.format(file_name))

    def mkdir(self):
        folder = os.path.exists(self.path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(self.path)  # makedirs 创建文件时如果路径不存在会创建这个路径


if __name__ == '__main__':
    # search_name, number, search_url, download_url, headers1, headers2
    search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&reqId=24b2acb0-e1f4-11e9-9c10-df22c38d9fb9'
    download_url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=320kmp3&from=web&t=1569668134762&reqId=717bbfe5-a891-49c2-b549-c923ea781cec'
    headers1 = {
        'Cookie': 'Cookie: _ga=GA1.2.1209502700.1578305434; _gid=GA1.2.570101734.1578305434; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1578305434; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1578305434; kw_token=EQ4EIPN5TE7',
        'Host': 'www.kuwo.cn',
        'csrf': 'EQ4EIPN5TE7',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E8%AE%B8%E5%B5%A9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    headers2 = {
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1569666496,1569668107; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1569677402',
        'Host': 'www.kuwo.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    path = r'D:\MUSIC\kuwo'
    while 1:
        print('输入搜索名称和下载数量：')
        get_input = input()
        index = get_input.split(' ')
        music = Music(index[0], int(index[1]), search_url, download_url, headers1, headers2, path)
        music.search()
        music.download()


