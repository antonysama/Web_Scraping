# -*- coding: utf-8 -*-
import scrapy


class ScrapeDfo2Spider(scrapy.Spider):
    name = 'scrape-dfo2'
    allowed_domains = ['www.canada.ca']
    # start_urls = ['https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=fisheriesoceans&start=&end=']

    def start_requests(self):
        yield scrapy.Request(url='https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=fisheriesoceans&start=&end=', callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})

    def parse(self, response):
        for quote in response.xpath('//*[@class="h5"]'):
            yield{
                'Date': quote.xpath('//p/time/text()').get(),
                'Title': quote.xpath('.//a/text()').get(),
                'Text': quote.xpath('.//following-sibling::p[2]/text()').get(),
                'Link': quote.xpath('.//a/@href').get(),
                'User-Agent': response.request.headers['User-Agent']}

        next_page_url = response.xpath('//a[@rel="next"]/@href').get()

        if next_page_url:
            yield scrapy.Request(url=response.urljoin(next_page_url), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
