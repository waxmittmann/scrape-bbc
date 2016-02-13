import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector

from scrapymasters.items import GuardianItem
from scrapymasters.util.string_util import string_util

class DmozSpider(CrawlSpider):
    name = "guardian"
    allowed_domains = ["bbc.com", "localhost"]
    # start_urls = ["http://www.bbc.com/"]
    start_urls = ["http://localhost:8090"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        articles = hxs.xpath("//*[contains(concat(' ', @class, ' '), ' media__content ')]")
        for article in articles:
            item = GuardianItem()

            item['title'] = string_util.get_first(
                    article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/text()") \
                    .extract(), "").strip(' \n')
            item['tags'] = string_util.get_first(
                    article.xpath("*[contains(concat(' ', @class, ' '), ' media__tag ')]/text()") \
                    .extract(), "").strip(' \n')
            item['summary'] = string_util.get_first(
                    article.xpath("*[contains(concat(' ', @class, ' '), ' media__summary ')]/text()") \
                    .extract(), "").strip(' \n')


            articleUrl = ''.join(article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/@href").extract())

            url = response.urljoin(articleUrl)

            yield scrapy.Request(url, callback=self.parse_dir_contents, meta=item)

    def parse_dir_contents(self, response):
        item = response.meta

        header = string_util.get_first(response.xpath("//*[contains(concat(' ', @class, ' '), ' story-body__h1 ')]/text()").extract(), "")\
            .strip(' \n')

        item['header'] = header
        item['url'] = response.url
        yield item
