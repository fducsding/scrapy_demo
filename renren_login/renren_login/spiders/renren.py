# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass


#这里的只是个方法，下面的url登不上去
    #重写是因为要发发送post请求
    #因为登录人人网需要账户密码，所以需要重写request
    def start_requests(self):
        url="http://www.renren.com/"
        data={"email":"970138074@qq.com","password":"pythonspider"}
        request=scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request


    def parse_page(self,response):
        with open("renren.html","w",encoding="utf-8") as fp:
            fp.write(response.text())
