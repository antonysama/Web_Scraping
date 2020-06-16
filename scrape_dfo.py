# -*- coding: utf-8 -*-
import scrapy


class ScrapeDfoSpider(scrapy.Spider):
    name = 'scrape-dfo'
    allowed_domains = ['canada.ca'] # get this one right
    start_urls = [
        'https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=fisheriesoceans&start=&end=']

    def parse(self, response):
        quotes = response.xpath('//*[@class="h5"]')
        for quote in quotes:
            title = quote.xpath('.//a/text()').extract_first()
            link = quote.xpath('.//a/@href').extract_first()

            yield {'Title': title,
                   'Link': link}

        next_page_url = response.xpath(
            '//a[@rel="next"]/@href').extract_first() # this "extract_first" is important
        #keep pagination outside the below for loop
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url))

        # quotes=response.xpath('//*[@class="h5"]/a[contains(text(), "haida")]')
        # quotes=response.xpath('//*[@class="h5"]/a[contains(., "canada")]')
        # quotes=response.xpath('//*[@class="h5"]/a[contains(.,"pacific") or (contains(.,"haida"))]')