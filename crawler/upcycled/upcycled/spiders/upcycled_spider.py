from scrapy import Spider, Request
from upcycled.items import UpcycledItem
from re import search, findall

class Upcycled_Spider(Spider):
	name = "upcycled"
	allowed_domains = ["mijnwebwinkel.nl"]
	start_urls = ["http://www.mijnwebwinkel.nl/winkel/shop-upcycled/"]  

	def parse(self, response):
		for url in response.xpath('//ul[contains(@class, "products")]/li/span/a/@data-product-url').extract():
			yield Request(url, callback=self.parse_product_details)


	def parse_product_details(self, response):
		product = response.xpath('//div[contains(@class, "article product")]')
		item = UpcycledItem()
		item['title'] = product.xpath('//h1[@class="product-title"]/text()').extract()[0].strip().encode('UTF-8')
		item['webshop_name'] = "Upcycled"
		item['webshop_logo'] = "http://upcycled.nl/img/upcycled-logo-klein-zwart-2.png"
		item['brand'] = "Upcycled"
		item['url'] = response.url
		item['description'] = '\n'.join(product.xpath('//div[@data-tab-content="description"]//p/text()').extract()).encode('UTF-8')
		item['product_cat'] = '|'.join(["Accessories", "Dames", "Tassen"])
		item['sizes'] = '|'.join(filter(lambda x: search(r'\d+', x), product.xpath('//table[@class="article-specs"]//td/text()').extract()))
		item['price'] = findall(r'\d+', ''.join(filter(lambda x: search(r'\d+', x), product.xpath('//div[@class="right"]//*[@class="pricetag"]//text()').extract())))[0]  + '.00'
		item['discount_price'] = item['price']
		item['image'] = product.xpath('//div[@class="left"]//img/@src').extract()[0]
		return item

