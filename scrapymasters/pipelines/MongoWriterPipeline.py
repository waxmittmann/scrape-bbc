from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils


class MongoWriterPipeline(object):
    def __init__(self):
        config = ConfigFiles.config()
        self.client = MongoUtils.create_client_from_config(config)
        self.db = self.client.scrape

    def process_item(self, article, spider):
        stripped_article = {
            "title": article["title"],
            "url": article["url"],
            "tags": article["tags"],
            "summary": article["summary"],
            "header": article["header"],
            "body": article["body"],
        }

        self.db.articles.update({"url": article["url"]}, stripped_article, upsert=True)
        return article

    def close_spider(self, spider):
        self.client.close()
