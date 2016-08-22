# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class UpcycledItem(Item):
	title = Field()
	url = Field()
	description = Field()
	webshop_name = Field()
	product_cat = Field()
	style = Field()
	image = Field()
	price = Field()
	discount_price = Field()
	sizes = Field()
	brand = Field()

