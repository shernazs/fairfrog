from scrapy.item import Item, Field


class IngarItem(Item):
    title = Field()
    url = Field()
    tags = Field()
    price = Field()
    sizes = Field()

