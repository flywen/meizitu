# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item

# 存储为json的pipeline
class JsonPipeline(object):
    def __init__(self):
        self.file = open('mzt.json','wb')
    # 将ensure_ascii设置为False，否则会存储成unicode
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()

# 存到mysql中
class MySqlPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'test',
                user = 'root',
                passwd = '',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
                )
    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self._conditional_insert,item)
        return item
    def _conditional_insert(self,tx,item):
        if item.get('title'):
            # item中的数据是一个title对应多个image_urls，故使用2个遍历
            for i in range(len(item['title'])):
                for j in range(len(item['image_urls'])):
                    tx.execute('insert into mzt values (%s,%s)',(item['title'][i],item['image_urls'][j]))
