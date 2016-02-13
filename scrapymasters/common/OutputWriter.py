import json
from pymongo import MongoClient
from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils

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
        # config = self.config
        # if config["username"] == "" and config["password"] == "":
        #     client = MongoClient("mongodb://" + config["url"] + "/" + config["dbname"])
        # else:
        #     client = MongoClient("mongodb://" + config["username"] + ":" + config["password"] + "@" + config["url"]
        #                          + "/" + config["dbname"])
        db = client.scrape
        db.articles.insert_one(data)
        client.close()
        print("Ending mongo write")