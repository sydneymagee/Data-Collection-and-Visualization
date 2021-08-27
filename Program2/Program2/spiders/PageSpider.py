"""
Sydney Magee
Program 2
Due: March 10 @ 1pm
"""
import scrapy

class PageSpider(scrapy.Spider):
    name = 'page'

    def start_requests(self):
        urls = ['https://www.equibase.com/static/entry/']
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        title = response.css('#page-bar > div > div > h1').extract_first()
        print(title)
        print(response.text)
        #pages = response.xpath('//*[@id="c-entries-index"]/div/table[2]/tbody')
        #print(pages)
