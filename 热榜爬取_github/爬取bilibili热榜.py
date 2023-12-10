import requests
import pandas
from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    #这里替换你的cookie
    #your cookie expected here
    'cookie':'cookie',
}


titlels,bvidls,authorls,pubdatels,viewls,coinls,likels,dislikels,rankls=[],[],[],[],[],[],[],[],[]


url= 'https://api.bilibili.com/x/web-interface/popular?'

def spider(pn):
    params = {
        'ps': '20',
        'pn': pn,
    }
    i = 0
    resp = requests.get(url, headers = headers, params = params).json()
    for data in resp['data']['list']:
        titlels.append(data['title'])
        bvidls.append(data['bvid'])
        authorls.append(data['owner']['name'])
        pubdatels.append(data['pubdate'])
        viewls.append(data['stat']['view'])
        coinls.append(data['stat']['coin'])
        likels.append(data['stat']['like'])
        dislikels.append(data['stat']['dislike'])
        i = i + 1
        rankls.append(i+(pn-1)*20)

for pn in range(1,6):
    spider(pn)

data = {
    '排名':rankls,
    '标题': titlels,
    'bv号':bvidls ,
    '作者': authorls,
    '日期':pubdatels,
    '观看数':viewls,
    '硬币数':coinls,
    '点赞数':likels,
    '点踩数':dislikels,
}
dataframe = pandas.DataFrame(data=data)
dataframe.to_csv('bilibili热榜.csv', index=False, encoding='utf_8_sig')