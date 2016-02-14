from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils


class MongoWriterPipeline(object):
    def __init__(self):
        config = ConfigFiles.config()
        self.client = MongoUtils.create_client_from_config(config)
        self.db = self.client.scrape

    def process_item(self, article, spider):
        self.db.articles.update({"url": article["url"]}, article, upsert=True)
        return article

    def close_spider(self, spider):
        self.client.close()
