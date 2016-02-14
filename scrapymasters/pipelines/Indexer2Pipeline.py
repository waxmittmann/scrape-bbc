from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils
from string import punctuation


class Indexer2Pipeline(object):
    def __init__(self):
        config = ConfigFiles.config()
        self.client = MongoUtils.create_client_from_config(config)
        self.db = self.client.scrape

    def process_item(self, article, spider):
        body = article['body']
        for word in body.split():
            word = word.strip(punctuation).lower()

            if len(word) != 0 and word.isalpha():
                url = article['url']
                #posts.update({'_id':213}, {'$set':{"jobs.1.title":1}}, upsert=False, multi=True)
                word_query = { "word": word }
                url_to_insert = {"$addToSet": {"urls": url }}
                self.db.words.update(word_query, url_to_insert, upsert=True, multi=True)

        return article

    def close_spider(self, spider):
        self.client.close()
