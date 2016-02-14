import scrapy
from scrapy.item import Field


class GuardianItem(scrapy.Item):
    title = Field()
    url = Field()
    tags = Field()
    summary = Field()
    header = Field()
    body = Field()
