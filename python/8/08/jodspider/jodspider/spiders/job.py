# -*- coding: utf-8 -*-
import scrapy
import re

from ..items import JodspiderItem
class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/list/170200,000000,0000,00,9,99,java,2,1.html','https://search.51job.com/list/170200,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        # 1.分离当前页面所有数据，存储到item中
        # 2.获取下一页链接，请求
        div_list = response.xpath('//div[@id="resultList"]/div[@class="el"]')
        # print(div_list)
        for div in div_list:
            # contains 只要属性包含某个值
            jobName = div.xpath('.//p[contains(@class,"t1")]/span/a/@title').extract_first('')
            # print(jobName)
            companyName = div.xpath('.//span[@class="t2"]/a/@title').extract_first('')
            # print(companyName)
            cityName = div.xpath('.//span[@class="t3"]/text()').extract_first('')
            # print(cityName)
            salary = div.xpath('.//span[@class="t4"]/text()').extract_first('')
            # print(salary)
            min_salary = 0
            max_salary = 0
            if u'年' in salary:
                money =  salary.split('万')[0].split('-')
                min_salary = int(money[0]) / 12
                min_salary = '%.1f' % min_salary
                max_salary = '%.1f' % (int(money[1]) / 12)
            elif u'万' in salary:
                money = salary.split('万')[0].split('-')
                min_salary = money[0]
                max_salary = money[1]
            elif u'千' in salary:
                money = salary.split('千')[0]
                if '-' in money:
                    min_salary = float(money.split('-')[0]) * 0.1
                    max_salary = float(money.split('-')[1]) * 0.1
                else:
                    min_salary = 0
                    max_salary = float(money) * 0.1
            elif u'日' in salary:
                money = salary.split('元')
                min_salary = 0
                max_salary =int( money[0]) * 30 / 10000
            else:
                min_salary = 0
                max_salary = 0

            date = div.xpath('.//span[@class="t5"]/text()').extract_first('')

            # item = JodspiderItem()
            # item['jobName'] = jobName
            # item['companyName'] = companyName
            # item['min_salary'] = min_salary
            # item['max_salary'] = max_salary
            # item['date'] = date
            # item['cityName'] = cityName
            #
            # yield item

        # next_url = response.xpath('//li[@class="bk"]/a[text()="下一页"]/@href').extract()
        # print('--------------------------')
        # print(next_url)
        # if len(next_url) != 0 :
        #     yield scrapy.Request(url = next_url[0],callback=self.parse)

        next_url = response.xpath('//div[@class="p_in"]/span/text()').extract_first('').split(',')[0]
        pattern = re.compile('(\d+)')
        result = re.findall(pattern,next_url)[0]
        # print(result)
        for page in range(1,int(result)+1):
            print(page)

            # 作业
# 获取总页码，然后在第一页和总页码中循环拼接url，并进行请求
# 2.站长图标，使用管道文件实现，下载图片，保存图片信息到文件中
#   红袖添香，使用管道文件实现， 下载图片，保存小说信息到文件中