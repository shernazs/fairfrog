from scrapy import Spider
from scrapy import *
from scrapy.selector import Selector
from ingar.items import IngarItem
import scrapy
import re


class StackSpider(Spider):
    name = "ingar"
    allowed_domains = ["ingar.nl"]
    start_urls = [
        "http://ingar.nl/shop/",
    ]

    def parse(self, response):
        for next_page in response.css("div[class*=bottom] > div > ul > li > a[class*=page-numbers]::attr('href')"):
            next_page = response.urljoin(next_page.extract())
            yield scrapy.Request(next_page, callback=self.parse)

        for product_link in response.css("section > div > div > div > a[class*=woocommerce-LoopProduct-link]::attr('href')"):
            product_link = response.urljoin(product_link.extract())
            yield scrapy.Request(product_link, callback=self.parse_product_details)

    def parse_product_details(self, response):
        if response.url != "http://ingar.nl/shop/peopletree-carrie-bolero-blauw/":
            pass

        #print ("SPIDER:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;::" + response.url)
        tags = response.css("div[id*=breadcrum] > a::text").extract()
        tags = tags[2:]
        tags = '|'.join(tags)
        title = response.css("h1::text").extract()[0]
        price = response.css("div[class*=price-block] > span[class*=woocommerce-Price-amount]::text").extract()
        print ("SHERNAZ:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;::" + str(price))
        if len(price) == 0:
            price = response.css("div[class*=price-block] > span[class*=woocommerce-Price-currencySymbol]::text").extract()
            print ("SHERNAZ:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;::" + str(price))
            if len(price) == 0:
                price = 0.0
            else:
                price = price[0]
                price = re.findall(r'\d+', price)[0]
        else:
            price = price[0]
            price = re.findall(r'\d+', price)[0]

        sizes = response.css("select[id*=maat] > option::attr('value')").extract()[1:]
        sizes = '|'.join(sizes)

        product = dict()
        product['url'] = response.url
        product['title'] = title
        product['tags'] = tags[2:]
        product['price'] = price
        product['sizes'] = sizes
        print (product)
        yield IngarItem(product)
