import scrapy
from scrapy.spiders import CrawlSpider

from scrapymasters.items import GuardianItem
from scrapymasters.util.stringutil import StringUtil
from scrapymasters.util.xpathutil import XpathUtil
from scrapymasters.postcrawl.completeProcessing import CompleteProcessing
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from pprint import pprint

from scrapymasters.postcrawl.Indexer import Indexer
from scrapymasters.postcrawl.FileWriter import FileWriter

class BBCSpider(CrawlSpider):
    name = "guardian"
    allowed_domains = ["bbc.com", "localhost"]
    # start_urls = ["http://www.bbc.com/"]
    start_urls = ["http://localhost:8090"]

    # def __init__(self):
    #     CompleteProcessing()
    #     dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse(self, response):
        articles = response.xpath("//" + XpathUtil.xpath_for_class('media__content'))
        for article in articles:
            item = GuardianItem()

            item['title'] = StringUtil.get_first(
                article.xpath(XpathUtil.xpath_for_class('media__title') + "/a/text()").extract(), "").strip(' \n')
            item['tags'] = StringUtil.get_first(
                article.xpath(XpathUtil.xpath_for_class('media__tag') + "/text()").extract(), "").strip(' \n')
            item['summary'] = StringUtil.get_first(
                article.xpath(XpathUtil.xpath_for_class('media__summary') + "/text()").extract(), "").strip(' \n')

            article_url = ''.join(article.xpath(XpathUtil.xpath_for_class("media__title") + "/a/@href").extract())

            url = response.urljoin(article_url)

            yield scrapy.Request(url, callback=self.parse_dir_contents, meta=item)

    def parse_dir_contents(self, response):
        item = response.meta

        header = StringUtil.get_first(
            response.xpath("//" + XpathUtil.xpath_for_class("story-body__h1") + "/text()").extract(), "").strip(' \n')

        body_list = response.xpath("//" + XpathUtil.xpath_for_class("story-body__inner") + "//p/text()").extract()
        body = ' '.join(body_list).strip(' \n')

        item['header'] = header
        item['url'] = response.url
        item['body'] = body
        yield item

    # def spider_closed(self, spider):
        # print("Spider done!")
        # l = dir(spider)
        # pprint(l)

        # print("State:")
        # l = dir(spider.state)
        # pprint(l)

        # print("Items: ")
        # print(type(spider.state.items()))
        # l = dir(spider.state.items())
        # pprint(l)

        # articles = spider.state.items()
        # index = Indexer.map_bodywords_to_articles(articles)
        #
        # print("Articles: ")
        # print(articles)
        #
        # articles_and_index = {
        #     'articles': articles,
        #     'index': index
        # }
        #
        # FileWriter.write_to_file(articles_and_index)

        # print(spider.state.get())
        # print(type(spider.crawler))
        # l = dir(spider.crawler)
        # pprint(l)