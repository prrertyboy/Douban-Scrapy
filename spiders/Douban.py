
        # -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,Spider
from scrapy.selector import Selector
from Doubanmovie.items import DoubanItem



class DoubanSpider(scrapy.Spider):
    name = 'DoubanSpider'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['http://https://movie.douban.com/top250/']

    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        movies = selector.xpath("//div[@class='info']")
        for movie in movies:
            titles = movie.xpath('.//span[@class="title"]/text()').extract()
            name = ''
            for title in titles:
            	name += title.strip()
            item['name'] = name
            item['score'] = movie.xpath('.//span[@class="rating_num"]/text()').extract()[0].strip()
            yield item

