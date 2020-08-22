# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from .items import QsbkItem
class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/2/']
    base_domain="https://www.qiushibaike.com"


    def parse(self, response):
        #返回的是一个列表
        duanzidivs=response.xpath("//div[@class='col1 old-style-col1']/div")
        # print(duanzidivs)


        for duanzidiv in duanzidivs:
            #stip()的作用是去掉上下行之间的空白字符
            author=duanzidiv.xpath(".//h2/text()").get().strip()
            #getall()的作用是把里面的内容提取出来转化成一个字符串并且返回一个列表
            content=duanzidiv.xpath(".//div[@class='content']//text()").getall()
            #上面的content是一个列表，用下面的方法就将content转化成一个字符串
            content="".join(content).strip()


            item=QsbkItem(author=author,content=content)
            # duanzi={"author":author,"content":content}
            # yield duanzi
            yield item

        yield scrapy.Request(self.base_domain + "/text/page/3/", callback=self.parse())
        # next_url=response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        # if not next_url:
        #     return
        # else:
        #     yield scrapy.Request(self.base_domain+next_url,callback=self.parse())

            # print(author)
            # print(content)