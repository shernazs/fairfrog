# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

url = "http://organicwear.nl/shop/"
class OrganicWearItem(Item):
	title = Field()
	description = Field()
	webshop_name = Field()
	product_cat = Field()
	style = Field()
	colors = Field()
	sizes = Field()
	price = Field()
	discount_price = Field()
	url = Field()
	images = Field()

