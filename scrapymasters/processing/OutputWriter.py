import json
from pymongo import MongoClient
import ConfigParser
import urllib

class OutputWriter:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("config.ini")

        self.url = config.get("Mongo", "url")
        self.username = config.get("Mongo", "username")
        self.password = config.get("Mongo", "password")
        self.dbname = config.get("Mongo", "dbname")

    @staticmethod
    def write_to_file(data):
        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)

    def write_to_mongo(self, data):
        print("Beginning mongo write")
        client = MongoClient("mongodb://" + self.username + ":" + self.password + "@" + self.url + "/" + self.dbname)
        db = client.scrape
        db.articles.insert_one(data)
        client.close()
        print("Ending mongo write")