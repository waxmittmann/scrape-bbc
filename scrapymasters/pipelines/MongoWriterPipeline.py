import json
from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils


class MongoWriterPipeline(object):
    def __init__(self):
        config = ConfigFiles.config()
        self.client = MongoUtils.create_client_from_config(config)
        self.db = self.client.scrape

# db.articles.update(
#   {"url": "http://localhost:8090/world-latin-america-35565085.html"},
#   {"body": "I am body", "url": "http://localhost:8090/world-latin-america-35565085.html", "tags": "Latin America & Caribbean", "summary": "Pope Francis and Russian Orthodox Patriarch Kirill call for restored Christian unity between the two churches at historic talks in Cuba.", "download_timeout": 180.0, "header": "Unity call as Pope Francis holds historic talks with Russian Orthodox Patriarch", "depth": 1, "download_latency": 0.028749942779541016, "download_slot": "localhost"},
#   {upsert: true}
# )
    def process_item(self, article, spider):
        self.db.articles.update({"url": article["url"]}, article, upsert=True)
        return article

    def close_spider(self, spider):
        self.client.close()
