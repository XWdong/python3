# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 封装GetData
class GetData:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
        self.submit = './submit.json'
    # 获取项目
    def GetDataList(self,urls):
        req = request.Request(urls, headers=self.header)
        res = request.urlopen(req)
        soup = BeautifulSoup(res, 'html5lib')
        # 得到目标信息
        items = soup.find_all('div', 'list-item')
        DataParam = {}

        for item in items:
            #项目名
            Title = item.find('div', 'project-title').get('title')
            #期限
            Term = item.find('div', 'project-day').find_next().span.get_text().strip()
            #项目金额
            Price = item.find('div', 'project-day').find_next().find_next_sibling().span.get_text().strip()
            #进度
            Speed = item.find_all('span')[-1].get_text().strip()
            #s收益
            Profit = item.find('div', 'year-money').find_next().find_next_sibling().span.get_text().strip()
            DataArray = []
            DataParam['Title']=Title
            DataParam['Term'] = Term
            DataParam['Price'] = Price
            DataParam['Speed'] = Speed
            DataParam['Profit'] = Profit
            print(DataParam)
#实例化类
spider = GetData()

urls = ['https://www.58klc.com/Borrow/index/p/{}'.format(str(i)) for i in range(1,5)]
for  item in urls:
    # print(titles)
    spider.GetDataList(item)

