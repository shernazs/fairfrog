from scrapy.item import Item, Field


class IngarItem(Item):
    title = Field()
    url = Field()
    description = Field()
    webshop_name = Field()
    product_cat = Field()
    style = Field()
    images = Field()
    tags = Field()
    price = Field()
    discount_price = Field()
    sizes = Field()
    colors = Field()
    brand = Field()

