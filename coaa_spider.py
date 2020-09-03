# -*- coding: utf-8 -*-
import scrapy


class CoaaSpiderSpider(scrapy.Spider):
    name = 'coaa_spider'
    allowed_domains = ['coaa.ab.ca']
    start_urls = [
        'https://www.coaa.ab.ca/library/category/best-practice-conferences/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="info-block"]')
        for quote in quotes:
            title = quote.xpath('.//div[2]/h3/text()').extract_first()
            type = quote.xpath('.//div[2]/h3/span/text()').extract_first()
            year = quote.xpath('.//div[3]/p[3]/text()').extract_first()
            link = quote.xpath('.//div/a/@href').extract_first()

            yield {'Title': title,
                   'Type': type,
                   'Year': year,
                   'Link': link}

        next_page_url = response.xpath(
            '//*[@class="next page-numbers"]/@href').extract_first()  # this "extract_first" is important
        # keep pagination outside the below for loop
        if next_page_url:
            yield scrapy.Request(next_page_url)
