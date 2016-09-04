# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class GeeskenvormgevingItem(Item):
	title = Field()
	url = Field()
	description = Field()
	webshop_name = Field()
	webshop_logo = Field()
	webshop_url = Field()
	product_cat = Field()
	image = Field()
	price = Field()
	discount_price = Field()
	sizes = Field()
	hashtags = Field()
	brand = Field()

