import json
from pymongo import MongoClient
import ConfigParser
import urllib

class OutputWriter:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("config.ini")
        # config.options("mongo")

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
        # mongodb://<username>:<password>@aws-us-east-1-portal.9.dblayer.com:10650,aws-us-east-1-portal.4.dblayer.com:11181/admin
        client = MongoClient("mongodb://" + self.username + ":" + self.password + "@" + self.url + "/" + self.dbname)
        db = client.scrape
        db.articles.insert_one(data)
        client.close()
        print("Ending mongo write")