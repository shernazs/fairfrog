from scrapy import Spider, Request
from organic_wear.items import OrganicWearItem
from re import search


class OrganicWear_Spider(Spider):
	name = "organic_wear"
	allowed_domains = ["organicwear.nl"]
	start_urls = ["http://organicwear.nl/shop/"]  


	def parse(self, response):
		for url in response.xpath('//ul[@class="products"]/li/a/@href').extract():
			yield Request(url, callback=self.parse_product_details)


	def parse_product_details(self, response):
		product = response.xpath('//div[@itemtype]')
		item = OrganicWearItem()
		item['title'] = product.xpath('//h1[@itemprop="name"]/text()').extract()[0]
		item['webshop_name'] = "Organic Wear"
		item['webshop_logo'] = "http://fairfrog.nl/wp-content/uploads/2016/08/OrganicWearLogo.png"
		item['webshop_url'] = "http://organicwear.nl/"
		item['brand'] = "Organic Wear"
		item['url'] = response.url
		item['description'] = '\n'.join(product.xpath('//div[@itemprop="description"]/p/text()').extract()[:-1]).encode('UTF-8')
		styles = filter(lambda x: search(r'[a-z]', x.lower()), [text.encode('UTF-8')[0] for text in product.xpath('//label[text()="Style"]/following-sibling::div/ul/li//text()').extract()])
		categories = ['-'.join(cat.split('-')[1:]) for cat in filter(lambda x: 'product_cat' in x, product.xpath('@class').extract()[0].split())]
		
		if 'M' in styles: categories.append("Heren")
		if 'W' in styles: categories.append("Dames")

		item['product_cat'] = '|'.join(categories)
		item['sizes'] = '|'.join(list(set(product.xpath('//label[text()="Size"]/following-sibling::div/ul/li/select/option/text()').extract())))
		item['price'] = product.xpath('//input[@class="cpf-product-price"]/@value').extract()[0] + '.00'
		item['discount_price'] = item['price']
		item['image'] = product.xpath('//div[@class="images"]/a/@href').extract()[0]
		item['hashtags'] = "Free postage within Groningen, The Netherlands"
		return item

