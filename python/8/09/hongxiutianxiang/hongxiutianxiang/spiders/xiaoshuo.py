# -*- coding: utf-8 -*-
import scrapy

from ..items import HongxiutianxiangItem
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/all?pageNum=1&pageSize=10&gender=2&catId=30008']

    def parse(self, response):
        li_list =response.xpath('//div[@class="right-book-list"]/ul/li')
        # print(li_list)
        for li in li_list:
            img = 'https:'+li.xpath('.//div[@class="book-img"]/a/img/@src').extract_first('')
            title = li.xpath('.//div[@class="book-img"]/a/img/@alt').extract_first('')
            author = li.xpath('.//div[@class="book-info"]/h4/a/text()').extract_first('')
            intro = li.xpath('.//p[@class="intro"]/text()').extract_first('')
            print(img)
            print(title)
            print(author)
            print(intro)

            item = HongxiutianxiangItem()
            item['img'] = [img]
            item['title'] = title
            item['author'] = author
            item['intro'] = intro

            yield item
