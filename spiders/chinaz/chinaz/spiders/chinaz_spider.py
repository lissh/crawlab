# -*- coding: utf-8 -*-
import scrapy
from chinaz.items import ChinazItem


class ChinazSpiderSpider(scrapy.Spider):
    name = 'chinaz_spider'
    allowed_domains = ['chinaz.com']
    start_urls = ['http://top.chinaz.com/hangye/']

    def parse(self, response):
        for item in response.css('.listCentent > li'):
            name = item.css('h3.rightTxtHead > a::text').extract_first()
            domain = item.css('h3.rightTxtHead > span::text').extract_first()
            description = item.css('p.RtCInfo::text').extract_first()
            rank = item.css('.RtCRateCent > strong::text').extract_first()
            rank = int(rank)
            yield ChinazItem(
                _id=domain,
                name=name,
                domain=domain,
                description=description,
                rank=rank,
            )

        # pagination
        a_list = response.css('.ListPageWrap > a::attr("href")').extract()
        url = 'http://top.chinaz.com/hangye/' + a_list[-1]
        yield scrapy.Request(url=url)
