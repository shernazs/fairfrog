from scrapy.item import Item, Field


class IngarItem(Item):
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
