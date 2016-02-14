from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils
from string import punctuation


class IndexerPipeline(object):
    def __init__(self):
        config = ConfigFiles.config()
        self.client = MongoUtils.create_client_from_config(config)
        self.db = self.client.scrape
        self.bulk = self.db.words.initialize_ordered_bulk_op()

    def process_item(self, article, spider):
        body = article['body']
        for word in body.split():
            word = word.strip(punctuation).lower()

            if len(word) != 0 and word.isalpha():
                url = article['url']
                word_query = { "word": word }
                url_to_insert = {"$addToSet": {"urls": url }}
                self.bulk.find(word_query).update(url_to_insert)
        return article

    def close_spider(self, spider):
        result = self.bulk.execute()
        print("Index write results:")
        print(result)
        self.client.close()
