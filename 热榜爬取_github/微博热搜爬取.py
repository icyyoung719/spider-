import requests
import pandas
from bs4 import BeautifulSoup

headers = {
    #这里替换你的cookie
    #your cookie expected here
    'cookie':'cookie',
    #'reference':'https://weibo.com/newlogin?tabtype=search&gid=&openLoginLayer=0&url=https%3A%2F%2Fwww.weibo.com%2F',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

url='https://weibo.com/ajax/side/hotSearch'
resp = requests.get(url, headers=headers).json()
titlelist,ranklist,hotlist,categorylist=[],[],[],[]
titlelist.append(resp['data']['hotgov']['name'])
ranklist.append("置顶")
hotlist.append(0)
categorylist.append("置顶榜单")
for data in resp['data']['realtime']:
    title=data['note']
    rank=data['rank']
    hot=data['raw_hot']
    category=data['category']
    titlelist.append(title)
    ranklist.append(rank+1)
    hotlist.append(hot)
    categorylist.append(category)
data = {
    '标题': titlelist,
    '排名': ranklist,
    '热度': hotlist,
    '类别':categorylist,
}
dataframe = pandas.DataFrame(data=data)
dataframe.to_csv('微博热榜.csv', index=False, encoding='utf_8_sig')