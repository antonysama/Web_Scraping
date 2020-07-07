# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class News4CrawlSpider(CrawlSpider):
    name = 'news4b_crawl'
    allowed_domains = ['news.gov.bc.ca']
    start_urls = ['https://archive.news.gov.bc.ca']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="newsRelease"]'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        yield{
            'c_title':response.xpath("//*[@colspan='2']/b/text()").get(),
            'date':response.xpath('//*[@style="width: 30%; vertical-align: top;"]/text()[3]').get(),
            'text':response.xpath('//*[@colspan="2"]/p/text()[1]').get,
        }