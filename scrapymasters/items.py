# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class GuardianItem(scrapy.Item):
    title = Field()
    url = Field()
    tags = Field()
    summary = Field()
    header = Field()