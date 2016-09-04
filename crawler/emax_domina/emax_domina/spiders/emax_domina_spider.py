from scrapy import Spider, Request
from emax_domina.items import EmaxDominaItem
from re import search, findall

class Emax_Domina_Spider(Spider):
	name = "emax_domina"
	allowed_domains = ["emaxdomina.nl"]
	start_urls = ["http://www.emaxdomina.nl/nl_nl/collectie/toepassing/"]  

	def parse(self, response):
		for next_page in response.xpath('//ul[@class="selector"]/li/div[@class="title"]/a/@href').extract():
			next_page = response.urljoin(next_page)
			yield Request(next_page, callback=self.parse)

		for url in response.xpath('//h3[@class="title"]/a/@href').extract():
			yield Request(response.urljoin(url), callback=self.parse_product_details)


	def parse_product_details(self, response):
		product = response.xpath('//ul[@class="list full"]')
		item = EmaxDominaItem()
		item['title'] = '-'.join(product.xpath('//h3[@class="title"]/text()').extract()[0].split('-')[:-1])
		item['webshop_name'] = "Emax Domina"
		item['webshop_logo'] = "http://fairfrog.nl/wp-content/uploads/2016/08/EmaxDominaLogo.png"
		item['webshop_url'] = "http://www.emaxdomina.nl/nl_nl/welkom/"
		item['image'] = response.urljoin(product.xpath('//div[@class="image"]/a/img/@src').extract()[0])
		item['brand'] = "Emax Domina"
		item['url'] = response.url
		item['description'] = product.xpath('//div[@class="text"]//text()').extract()[0].encode('UTF-8')
		item['product_cat'] = response.xpath('//ul[@class="selector"]/li/div[@class="title"]/a/text()').extract()[0]
		size = product.xpath('//div[@class="size"]/text()').extract()
		if size: item['sizes'] = '|'.join(size).encode('UTF-8')
		else: item['sizes'] = ''
		prices = findall(r'(\d+,\d+)', '|'.join(product.xpath('//div[contains(@class, "price")]/text()').extract()).encode('UTF-8'))
		item['price'] = prices[0].replace(',', '.')
		if len(prices) > 1:
			item['discount_price'] = prices[1]
		else:
			item['discount_price'] = item['price'].replace(',', '.')
		return item

