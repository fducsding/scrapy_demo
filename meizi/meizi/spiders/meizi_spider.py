# -*- coding: utf-8 -*-
import scrapy
from meizi.items import  MeiziItem
import json

class MeiziSpiderSpider(scrapy.Spider):
    name = 'meizi_spider'
    allowed_domains = ['image.baidu.com']


    #重写start_urls，按照我们自己的需求
    def start_requests(self):
        for i in range(30,120,30):
            url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9F%AF%E5%8D%97&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E6%9F%AF%E5%8D%97&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30".format(i)
            # 交给调度器
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        imgs=json.loads(response.body).get("data")     #json文件是一个字典
        # print(imgs),imgs是一个列表
        for img in imgs:
            item=MeiziItem()
            item['image_urls']=[img['middleURL']]
            print(img['middleURL'])
            yield(item)






