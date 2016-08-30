from scrapy import Spider, Request
from hetgroeneshaap.items import HetGroeneSchaapItem
from re import findall


class HetGroeneSchaap_Spider(Spider):
	name = "hetgroeneshaap"
	allowed_domains = ["hetgroeneschaap.nl"]
	start_urls = ["http://www.hetgroeneschaap.nl/c-3271058/producten/"]  


	def parse(self, response):
		for url in response.xpath('//ul[contains(@class, "products")]/li//a/@data-product-url').extract():
			yield Request(url, callback=self.parse_product_details)


	def parse_product_details(self, response):
		product = response.xpath('//div[contains(@class, "product-page")]')
		item = HetGroeneSchaapItem()
		item['title'] = product.xpath('//h1[@class="product-title"]/text()').extract()[0].strip()
		item['webshop_name'] = "Het Groene Schaap"
		item['webshop_logo'] = "https://static.mijnwebwinkel.nl/winkel/het-groene-schaap/nl_NL_image_header_4.png?t=1471936616"
		item['brand'] = "Het Groene Schaap"
		item['url'] = response.url
		item['description'] = ' '.join(product.xpath('//div[@data-tab-content="description"]//text()').extract()).strip()
		item['product_cat'] = 'Kinderen'
		item['sizes'] = '|'.join(product.xpath('//label[contains(text(),"Maat")]//option[@value > 0]/text()').extract())
		prices = findall(r'\d+.\d+', ''.join(product.xpath('//*[@class="pricetag"]//text()').extract()).encode('UTF-8').replace(',','.'))
		item['price'] = prices[0]
		if len(prices) > 1:
			item['discount_price'] = prices[1]
		else:
			item['discount_price'] = item['price']
		item['image'] = product.xpath('//div[@class="images"]//img/@src').extract()[0]
		item['hashtags'] = ''.join(product.xpath('//a[contains(@class,"badge")]//text()').extract()).strip().encode('UTF-8')
		return item

