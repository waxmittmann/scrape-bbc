import json
from pprint import pprint


class IndexerPipeline(object):
    # vat_factor = 1.15

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        # with open('guardian-articles.json') as data_file:
        # articles = json.load(data_file)
        for article in item:
            print("Processing ")
            print(article)
