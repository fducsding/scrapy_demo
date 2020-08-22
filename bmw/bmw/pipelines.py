# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
# from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from bmw import settings
#需要下载pillow模块


'''
#这是传统的方法分种类下载图片
class BmwPipeline:

    def __init__(self):

        #因为后期要用到images_path，把其改为self.path这个属性
        # #括号里的可以获取到pipe.py文件的目录
        # os.path.dirname(__file__)
        # #但是还要拿到第一个bmw文件的目录，所以传入里面
        # os.path.dirname(os.path.dirname(__file__))
        #构建bmw文件夹下images文件夹路径
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"images")
        #如果bmw下不存在images文件夹
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        # print(self.path)


    def process_item(self, item, spider):
        category=item["category"]
        urls=item["urls"]
        #创建分类的文件夹
        category_path=os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)


        for url in urls:
            #url地址按 _ 进行分割后然后取最后一个
            image_name=url.split("_")[-1]
            # print(image_name)
            request.urlretrieve(url,os.path.join(category_path,image_name))

        return item

'''






'''
#使用scrapy自带的方法要在settings.py文件中将
ITEM_PIPELINES = {
   'bmw.pipelines.BmwPipeline': 300,将这句注释掉
#在settings.py中添加图片下载的路径，供images pipelines使用
 IMAGES_STORE=os.path.join(os.path.dirname(os.path.dirname(__file__)),"images")
#并且如果需要按照分类保存图片，我们还需要重写ImagesPipeline
'''


#重写ImagesPipeline这个类中,按照自己的需求来写，它本身是图片全部下下来，不是分类
#继承ImagesPipeline这个类
class BMWImagesPipeline(ImagesPipeline):
    #这个方法是在发送下载请求之前调用
    #其实这个方法本身就是去发送下载请求的
    def get_media_requests(self, item, info):
        request_objs=super(BMWImagesPipeline,self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item=item
        return request_objs



    #def file_path(self, request, response=None, info=None):
    #这个方法是在图片将要被存储的时候调用，来获取图片存储的路径
    def file_path(self, request, response=None, info=None):
        #file_path返回的图片名字
        path=super(BMWImagesPipeline,self).file_path(request,response,info)
        category=request.item.get("category")
        images_store=settings.IMAGES_STORE
        category_path=os.path.join(images_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name=path.replace("full/","")
        image_path=os.path.join(category_path,image_name)
        return image_path
