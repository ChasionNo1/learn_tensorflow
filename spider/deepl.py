import requests
from lxml import etree
'''
用解析库解析
'''

url = 'https://dict.deepl.com/english-chinese/search?ajax=1&source=english&onlyDictEntries=1&translator=dnsof7h3k2lgh3gda&delay=800&jsStatus=0&kind=full&eventkind=change&forleftside=true'
data = {'query': 'problems'}
response = requests.post(url=url, data=data)
print(response.text)
html_source = response.text
html = etree.HTML(html_source)
# 获得翻译结果
result = html.xpath('//div/span/a/text()')
print(result)
