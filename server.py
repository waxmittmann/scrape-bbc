#!/usr/bin/env python
import web
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapymasters.spiders.BBCSpider import BBCSpider
from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils

urls = (
    '/words/(.+)', 'WordsGetOne',
    '/articles', 'Articles',
    '/words', 'Words',
)

app = web.application(urls, globals())


class Articles:
    def __init__(self):
        self.config = ConfigFiles.config()

    def GET(self):
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        articles = MongoUtils.find_all_articles(db)
        # articles = db.articles.find()
        client.close()
        return articles

    def PUT(self):
        runner = CrawlerRunner()
        runner.crawl(BBCSpider)
        d = runner.join()
        # d.addBoth(lambda _: reactor.stop())

        reactor.run(installSignalHandlers=0) # the script will block

        # process = CrawlerProcess({
        #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        # })
        #
        # process.crawl(BBCSpider)
        # process.start() # the script will block here until the crawling is finished

class WordsGetOne:
    def __init__(self):
        self.config = ConfigFiles.config()

    def GET(self, word):
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        articles = MongoUtils.find_article_by_word(db, word)
        client.close()
        return articles


class Words:
    def __init__(self):
        self.config = ConfigFiles.config()

    def GET(self):
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        words = MongoUtils.find_all_words(db)
        client.close()
        return words

if __name__ == "__main__":
    app.run()
