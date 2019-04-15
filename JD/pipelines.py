# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl


class JdPipeline(object):
    f = None
    sheet1 = None

    def open_spider(self, spider):
        self.f = openpyxl.Workbook()  # 创建excel连接对象
        self.ws = self.f.active  # 创建excel表1
        self.ws.append(["ID", "Title", "Link", "Price", "Shop_name", "Comments"])

    def process_item(self, item, spider):
        # 将title进行处理, title是列表, 需要转换为字符串
        item["title"] = "-".join(item["title"])

        # 处理没有店铺名字的情况
        if not item["shop_name"]:
            item["shop_name"] = "海外全球购"

        line = [item['id'], item['title'], item['link'], item['price'], item['shop_name'], str(item['comments'])]
        self.ws.append(line)

        return item

    def close_spider(self, spider):
        print('存储结束')
        self.f.save("JdDemo.xlsx")
