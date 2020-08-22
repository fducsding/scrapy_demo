# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BmwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    #传统的方法
    '''
        category=scrapy.Field()
        urls = scrapy.Field()
    '''



    #scrapy中自带的方法
    category = scrapy.Field()
    image_urls=scrapy.Field()
    iamges=scrapy.Field()
