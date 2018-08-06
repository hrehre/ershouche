# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Youxin1Item(scrapy.Item):
    # define the fields for your item here like:

    collections = 'ershouche'
    title = scrapy.Field()  # 标题
    price = scrapy.Field()  # 原价
    current_price = scrapy.Field()  # 当前价格
    payment = scrapy.Field()  # 首付
    month_payment = scrapy.Field()  # 月供
    time = scrapy.Field()  # 上牌时间
    kilometer = scrapy.Field()  # 公里数
    displacement = scrapy.Field()  # 排量
    image = scrapy.Field()  # 图片
    color = scrapy.Field()  # 颜色
    type = scrapy.Field()  # 类型
    motor = scrapy.Field()  # 发动机
    gearbox = scrapy.Field()  # 变速箱
    area = scrapy.Field()  # 区域
    car_id = scrapy.Field()  # 车辆的id
