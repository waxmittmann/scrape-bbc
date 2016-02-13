from pymongo import MongoClient


class MongoUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_client_from_config(config):
        if config["username"] == "" and config["password"] == "":
            client = MongoClient("mongodb://" + config["url"] + "/" + config["dbname"])
        else:
            client = MongoClient("mongodb://" + config["username"] + ":" + config["password"] + "@" + config["url"]
                             + "/" + config["dbname"])
        return client
