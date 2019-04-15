# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 商品数据的id
    title = scrapy.Field()  # 商品名字
    link = scrapy.Field()   # 商品连接
    price = scrapy.Field()  # 价格
    comments = scrapy.Field()   # 评论数
    shop_name = scrapy.Field()  # 商家的名字