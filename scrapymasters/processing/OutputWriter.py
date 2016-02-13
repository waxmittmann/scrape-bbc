import json
from pymongo import MongoClient
import ConfigParser

class OutputWriter:
    url = None
    username = None
    password = None

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("config.ini")
        config.options("mongo")

        self.url = config.get("Mongo", "url")
        self.username = config.get("Mongo", "username")
        self.password = config.get("Mongo", "password")

    @staticmethod
    def write_to_file(data):
        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)

    @staticmethod
    def write_to_mongo(self, data):

        # mongodb://<username>:<password>@aws-us-east-1-portal.9.dblayer.com:10650,aws-us-east-1-portal.4.dblayer.com:11181/admin
        client = MongoClient("mongodb://" + self.username + ":" + self.password + "@" + self.url + "/admin")

