# -*- coding: utf-8 -*-

# Scrapy settings for meizi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'meizi'

SPIDER_MODULES = ['meizi.spiders']
NEWSPIDER_MODULE = 'meizi.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
  "referer":"http://image.baidu.com/search/",
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

ITEM_PIPELINES = {
   # 'meizi.pipelines.MeiziPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline':1
}

IMAGES_STORE = "E:/meizi/"
# IMAGES_URLS_FIELD='URL'
# LOG_FILE="scrapy.log"    将爬取的状态保存到scrapy.log里面