# -*- coding: utf-8 -*-

# Scrapy settings for meizitu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meizitu (+http://www.yourdomain.com)'

# 要使用的pipelines
ITEM_PIPELINES = {
        'meizitu.pipelines.JsonPipeline': 300,                 #存储为json
        'meizitu.pipelines.MySqlPipeline':400,                 #存储到数据库
        'scrapy.contrib.pipeline.images.ImagesPipeline':1,     #使用imagespipeline（内置的pipeline，无需在pipelines.py中定义）来存储图片
}

#定义图片存储路径
IMAGES_STORE = 'D:/temp/mzt'
