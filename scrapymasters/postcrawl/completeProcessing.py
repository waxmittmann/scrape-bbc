from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.spiders import CrawlSpider


class CompleteProcessing(CrawlSpider):
    def __init__(self):
        print("Initing")
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print("Spider done!")
        print(spider)