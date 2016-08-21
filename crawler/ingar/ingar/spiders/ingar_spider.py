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

        tags = response.css("div[id*=breadcrum] > a::text").extract()
        tags = '|'.join(tags[2:])
        title = response.css("h1::text").extract()[0]
        price = response.css("div[class*=price-block] > span[class*=woocommerce-Price-amount]::text").extract()
        brand = response.css("ul[class*=product-tabs] > li > a::text").extract()[0]
        #TODO: We might wanna extract original prices, if price is disconted
        if len(price) == 0:
            price = response.css("div[class*=price-block] > ins > span[class*=woocommerce-Price-amount]::text").extract()
            if len(price) == 0:
                price = 0.0
            else:
                price = price[0]
                price = findall(r'\d+', price)[0]
        else:
            price = price[0]
            price = findall(r'\d+', price)[0]

        sizes = response.css("select[id*=maat] > option::attr('value')").extract()[1:]
        sizes = '|'.join(sizes)

        img = response.css("img[class*=wp-post-image]::attr('src')").extract()[0]

        product = dict()
        product['url'] = response.url
        product['title'] = title
        product['tags'] = tags
        product['price'] = price
        product['sizes'] = sizes
        product['img'] = img
        product['brand'] = brand
        print (product)
        yield IngarItem(product)
