from scrapy import Spider
from scrapy import *
from scrapy.selector import Selector
from ingar.items import StackItem
import scrapy



class StackSpider(Spider):
    name = "ingar"
    allowed_domains = ["ingar.nl"]
    start_urls = [
        "http://ingar.nl/shop/",
    ]

    def parse(self, response):
        for next_page in response.css("div[class*=bottom] > div > ul > li > a[class*=page-numbers]::attr('href')"):
            next_page = response.urljoin(next_page.extract())
            print ("SHERNAZ:::::::::::::::::::::::::::::::::::::::::::::::::::::::::NEXT PAGE::::;::" + next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        for product_link in response.css("section > div > div > div > a[class*=woocommerce-LoopProduct-link]::attr('href')"):
            product_link = response.urljoin(product_link.extract())
            #print ("SHERNAZ:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;::" + url)
            yield scrapy.Request(product_link, callback=self.parse_product_details)




    def parse_product_details(self, response):
        #print "ALOK:: Got product page response:: TODO write parser"
        pass
        '''questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
            '''
