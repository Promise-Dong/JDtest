# -*- coding: utf-8 -*-
import scrapy
import json
from JD.items import JdItem


class JddemoSpider(scrapy.Spider):
    name = 'jddemo'

    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&enc=utf-8']
    comments_urls = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="

    def parse(self, response):
        li_list = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for li in li_list:
            try:
                id = li.xpath('./div/div[6]/a/@data-sku').extract_first()
                title = li.xpath('./div/div[4]/a/em/text()').extract()
                link = li.xpath('./div/div[1]/a/@href').extract_first()
                price = li.xpath('./div/div[3]/strong/i/text()').extract_first()
                # comments = li.xpath('./div/div[5]/strong/a//text()').extract_first()
                shop_name = li.xpath('./div/div[7]/span/a/text()').extract_first()

                item = JdItem()

                item["id"] = id
                item["title"] = title
                item["link"] = link
                item["price"] = price
                # self.item["comments"] = comments
                item["shop_name"] = shop_name

            except:
                raise Exception("解析异常!!!")
            yield scrapy.Request(url=self.comments_urls + str(id), callback=self.getDetailpage, meta={"item": item})

    def getDetailpage(self, response):
        item = response.meta["item"]
        js = json.loads(str(response.body.decode(response.encoding)))

        item["comments"] = js["CommentsCount"][0]["CommentCountStr"]

        yield item
