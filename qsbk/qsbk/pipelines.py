# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class QsbkPipeline:
#     def __init__(self):
#         self.fp=open("duanzi.json","w",encoding="utf-8")
#
#     def open_spider(self,spider):
#         print("这是爬虫开始了")
#
#
#     def process_item(self, item, spider):
#         #改为False才能保存中文
#         item_json=json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')  #换行
#         return item
#
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print("爬虫结束了")


#    这个方法保存的是一个列表，列表里就一个字典，所有的数据都保存在这一个字典里
#下面的是优化存储方式
#引入一个json形式的导出
# from scrapy.exporters import JsonItemExporter
#
# class QsbkPipeline:
#     def __init__(self):
#         #wb是以二进制方式打开，因为JsonItemExporter在写入数字时是以bite形式写入
#         self.fp=open("duanzi.json","wb")
#         self.exporter=JsonItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
#         self.exporter.start_exporting()
#
#     def open_spider(self,spider):
#         print("这是爬虫开始了")
#
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了")






from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline:
    def __init__(self):
        #wb是以二进制方式打开，因为JsonItemExporter在写入数字时是以bite形式写入
        self.fp=open("duanzi.json","wb")
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")


    def open_spider(self,spider):
        print("这是爬虫开始了")


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了")























