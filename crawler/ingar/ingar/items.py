from scrapy.item import Item, Field


class IngarItem(Item):
    title = Field()
    url = Field()
    img = Field()
    tags = Field()
    price = Field()
    sizes = Field()

