# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from meizitu.items import MeizituItem

class MeiZiTu(CrawlSpider):
    name = 'mzt'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com']

    rules = (
            # 遇到这种链接就使用函数parse_item来处理
            Rule(LinkExtractor(allow=('http://www.meizitu.com/a/\d*?\.html')),callback='parse_item'),
            # 遇到这种链接就follow（没有callback会默认follow）
            Rule(LinkExtractor(allow=('list_1'))),
            )

    def parse_item(self,response):
        sel = Selector(response)
        items = []
        item = MeizituItem()
        # 提取title和image_urls
        item['title'] = sel.xpath('//*[@id="maincontent"]/div[2]/div[1]/h2/a/text()').extract()
        item['image_urls'] = sel.xpath('//*[@id="picture"]/p/img/@src').extract()
        items.append(item)
        #yield item
        # 返回到item
        return items

