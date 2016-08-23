from scrapy import Spider, Request
from ingar.items import IngarItem
from re import findall


class StackSpider(Spider):
	name = "ingar"
	allowed_domains = ["ingar.nl"]
	start_urls = [
	"http://ingar.nl/shop/",
	]


	def parse(self, response):
		for next_page in response.xpath('//a[@class="page-numbers"]/@href'):
			next_page = response.urljoin(next_page.extract())
			yield Request(next_page, callback=self.parse)

		for product_link in response.xpath('//a[@class="woocommerce-LoopProduct-link"]/@href'):
			product_link = response.urljoin(product_link.extract())
			yield Request(product_link, callback=self.parse_product_details)


	def parse_product_details(self, response):
		categories = '|'.join(filter(lambda x: x != 'SALE', response.xpath('//*[@class="posted_in"]/a/text()').extract()))
		title = response.css("h1::text").extract()[0]
		brand = response.css("ul[class*=product-tabs] > li > a::text").extract()[0]
		sizes = '|'.join(response.xpath('//select[@id="maat"]//text()')[1:].extract())
		img = response.xpath('//a[contains(@class, "woocommerce-main-image")]/@href').extract()[0]
		product = IngarItem()
		product['url'] = response.url
		product['title'] = title
		product['description'] = '\n'.join(response.xpath('//div[contains(@class, "product-shop")]/p/text()').extract()).encode('UTF-8')
		product['product_cat'] = categories
		tags = response.xpath('//span[contains(@class,"label-icon")]/text()').extract()
		if tags:
			product['tags'] = tags[0]

		#TODO: We might wanna extract original prices, if price is disconted
		prices = findall(r'(\d+.\d+)', '|'.join(response.xpath('//p[@class="price"]//span[contains(@class, "woocommerce-Price-amount")]/text()').extract()).encode('UTF-8'))
		product['price'] = prices[0]
		if len(prices) > 1:
			product['discount_price'] = prices[1]
		else:
			product['discount_price'] = product['price']
		product['sizes'] = sizes
		product['image'] = img
		product['brand'] = brand
		product['webshop_name'] = "Ingar"
		product['webshop_logo'] = "http://ingar.nl/wp-content/uploads/shop/Ingar-logo2.png"
		yield product
