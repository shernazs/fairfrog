from scrapy import Spider, Request
from scrapy_tutorial.items import UpcycledItem
from re import search

class Upcycled_Spider(Spider):
	name = "upcycled"
	allowed_domains = ["http://www.mijnwebwinkel.nl"]
	start_urls = ["http://www.mijnwebwinkel.nl/winkel/shop-upcycled/"]  

	def parse(self, response):
		for url in response.xpath('//ul[contains(@class, "products")]/li/div/a/@href').extract():
			yield Request(url, callback=self.parse_product_details)


	def parse_product_details(self, response):
		product = response.xpath('//div[contains(@class, "article product")]')
		item = UpcycledItem()
		item['product_title'] = product.xpath('//h1[@class="product-title"]/text()').extract()[0]
		item['webshop_name'] = "Upcycled"
		item['url'] = response.url
		item['description'] = '\n'.join(product.xpath('//div[@data-tab-content="description"]//p/text()').extract()).encode('UTF-8')
		item['product_cat'] = ["Tassen"]
		item['product_tags'] = item['product_cat']
		item['style'] = ["W"]
		item['color'] = ""
		item['size'] = list(set(product.xpath('//label[text()="Size"]/following-sibling::div/ul/li/select/option/text()').extract()))
		item['price'] = product.xpath('//div[@class="right]/').extract()[0]
		item['discount_price'] = item['price']
		item['images'] = product.xpath('//div[@class="left"]//img/@src').extract()
		return item


	"""	
	def parse(self, response):
		filename = response.url.split('/')[-2] + ".html"
		with open (filename, 'wb') as f:
			f.write(response.body)
	"""


