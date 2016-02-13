import json
from pprint import pprint


class IndexerPipeline(object):
    # vat_factor = 1.15

    def __init__(self):
        self.article_word_index = {}

    def process_item(self, item, spider):
        print("Got: " + str(item))
        return item
        # print(item)
        # with open('guardian-articles.json') as data_file:
        # articles = json.load(data_file)

        # for article in item:
        #     print("Processing: ")
        #     print(article)
        #
        #     if type(article) is list:
        #         for i in article:
        #             yield i
        #     else:
        #         yield article
            # print("Processing ")
            # print(article)
            # yield article
