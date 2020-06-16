# -*- coding: utf-8 -*-
import scrapy


class CanadaSpider(scrapy.Spider):
    name = 'canada'
    allowed_domains = ['canada.ca']
    start_urls = ['https://www.canada.ca/en/news/advanced-news-search/news-results.html?start=&typ=newsreleases&end=&idx=0&dprtmnt=fisheriesoceans']

    page_count = 0

    def start_requests(self):
        for i in range(self.page_count, 690, 10):
            yield scrapy.Request('https://www.canada.ca/en/news/advanced-news-search/news-results.html?start=&typ=newsreleases&end=&idx=%d&dprtmnt=fisheriesoceans'%i, callback=self.parse
            )

    def parse(self, response):

        quotes = response.xpath('//*[@class="h5"]')
        for quote in quotes:
            title = quote.xpath('.//a/text()').extract_first()
            link = quote.xpath('.//a/@href').extract_first()

            yield {'Title': title,
               'Link': link}