import json
from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils


# Todo: Consider removing this
class OutputWriter:
    def __init__(self):
        self.config = ConfigFiles.config()

    @staticmethod
    def write_to_file(data):
        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)

    def write_to_mongo(self, data):
        print("Beginning mongo write")
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        db.articles.insert_one(data)
        client.close()
        print("Ending mongo write")