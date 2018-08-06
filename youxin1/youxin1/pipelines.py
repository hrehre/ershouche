# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from youxin1.items import Youxin1Item


class Youxin1Pipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    '''
    连接mongdb存储数据
    '''
    def __init__(self):
        coon = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        db = coon[settings['MONGODB_DB']]
        self.collection = db[Youxin1Item.collections]

    def process_item(self, item, spider):
        if isinstance(item, Youxin1Item):
            self.collection.update({'car_id': item['car_id']}, {'$set': item}, True)
            return item
