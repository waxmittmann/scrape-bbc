import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from scrapymasters.items import GuardianItem


class DmozSpider(CrawlSpider):
    name = "guardian"
    allowed_domains = ["bbc.com", "localhost"]
    # start_urls = ["http://127.0.0.1:8742/Guardian_10_02_2016.html"]
    # start_urls = ["http://www.theguardian.com/"]
    # start_urls = ["http://www.bbc.com/"]
    start_urls = ["http://localhost:8090"]

    # articles = hxs.xpath("//*[contains(concat(' ', @class, ' '), ' media__content ')]")
    # <div class="media__content">
    #         <h3 class="media__title">
    #             <a class="media__link" href="/news/world-latin-america-35565085"
    #                       rev="hero1|headline" >
    #                                                 Pope in historic Russia church talks                                                    </a>
    #         </h3>
    #
    #                                 <p class="media__summary">
    #                                                 Pope Francis and Russian Orthodox Patriarch Kirill call for restored Christian unity between the two churches at historic talks in Cuba.                                                    </p>
    #
    #                                 <a class="media__tag tag tag--news" href="/news/world/latin_america"
    #                       rev="hero1|source" >Latin America &amp; Caribbean</a>
    #
    #     </div>
    #
    #     <a class="block-link__overlay-link"
    #        href="/news/world-latin-america-35565085"
    #               rev="hero1|overlay"                    tabindex="-1"
    #        aria-hidden="true">
    #         Pope in historic Russia church talks                </a>
    # </div>

    # //*[contains(concat(' ', @class, ' '), ' Test ')]
    # //*[contains(concat(' ', @class, ' '), ' fc-item ')]/*[contains(concat(' ', @class, ' '), ' fc-item__link ')]
    # //*[contains(concat(' ', @class, ' '), ' fc-item ')]/*[contains(concat(' ', @class, ' '), ' fc-item__link ')/*[contains(concat(' ', @class, ' '), ' fc-item__kicker ')]
    def parse(self, response):
        print(response)
        hxs = HtmlXPathSelector(response)
        # articles = hxs.xpath("//*[contains(concat(' ', @class, ' '), ' fc-item ')]")
        articles = hxs.xpath("//*[contains(concat(' ', @class, ' '), ' media__content ')]")
        for article in articles:
            # item = GuardianItem()
            print("\n{--\n" + article.extract() + "\n--}\n")
            # item['title'] = article.xpath("//*[contains(concat(' ', @class, ' '), ' fc-item__link ')]/@href").extract()
            # item['url'] = article.xpath("//*[contains(concat(' ', @class, ' '), ' fc-item__link ')]"
            #                                "//*[contains(concat(' ', @class, ' '), ' fc-item__kicker ')]/text()").extract()

            # item['title'] = DmozSpider.get_first(article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/text()") \
            #         .extract(), "").strip(' \n')
            # item['url'] = DmozSpider.get_first(article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/@href") \
            #         .extract(), "").strip(' \n')
            # item['tags'] = DmozSpider.get_first(article.xpath("*[contains(concat(' ', @class, ' '), ' media__tag ')]/text()") \
            #         .extract(), "").strip(' \n')
            # item['summary'] = DmozSpider.get_first(article.xpath("*[contains(concat(' ', @class, ' '), ' media__summary ')]/text()") \
            #         .extract(), "").strip(' \n')

            meta_map = {
                'title': DmozSpider.get_first(
                    article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/text()") \
                    .extract(), "").strip(' \n'),
                'tags': DmozSpider.get_first(
                    article.xpath("*[contains(concat(' ', @class, ' '), ' media__tag ')]/text()") \
                    .extract(), "").strip(' \n'),
                'summary': DmozSpider.get_first(
                    article.xpath("*[contains(concat(' ', @class, ' '), ' media__summary ')]/text()") \
                    .extract(), "").strip(' \n')}
            # url = DmozSpider.get_first(article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/@href") \
            #         .extract(), "").strip(' \n')

            articleUrl = ''.join(article.xpath("*[contains(concat(' ', @class, ' '), ' media__title ')]/a/@href").extract())
            print("Trying to link: " + ''.join(articleUrl))
            url = response.urljoin(articleUrl)

            yield scrapy.Request(url, callback=self.parse_dir_contents, meta=meta_map)

            # print(item)
            # yield item

    # class scrapy.http.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])
    def parse_dir_contents(self, response):
        meta_map = response.meta

        header = DmozSpider.get_first(response.xpath("*[contains(concat(' ', @class, ' '), ' story_body__h1 ')]").extract(), "")\
            .strip(' \n')

        item = GuardianItem()
        item['title'] = meta_map['title']
        item['tags'] = meta_map['tags']
        item['summary'] = meta_map['summary']
        item['header'] = header
        yield item

    @staticmethod
    def get_first(list, ifEmpty):
        if len(list) > 0:
            return list[0]
        else:
            return ifEmpty
