from pymongo import MongoClient


class MongoUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_client_from_config(config):
        if config["username"] == "" and config["password"] == "":
            client = MongoClient("mongodb://" + config["url"] + "/" + config["dbname"])
            print("Using " + "mongodb://" + config["url"] + "/" + config["dbname"])
        else:
            client = MongoClient("mongodb://" + config["username"] + ":" + config["password"] + "@" + config["url"]
                             + "/" + config["dbname"])
        return client

    @staticmethod
    def find_article_by_url(db, url):
        # pipeline = [
        #     {"$unwind" : "$articles"},
        #     {"$match" : {"articles.url": url}},
        #     {"$project" :
        #          {"_id" : 0,
        #          "url" : "$articles.url",
        #          "body" : "$articles.body",
        #          "tags" : "$articles.tags",
        #          "summary" : "$articles.summary",
        #          "title" : "$articles.title"}}
        # ]

        print("Finding by " + url)

        # cursor = db.articles.aggregate(pipeline)

        cursor = db.articles.find({"url": url})

        result = []
        for item in cursor:
            print("Item is: ")
            print(item)
            result.append(item)

        return result

    @staticmethod
    def find_article_by_word(db, word):
        word_index = db.words.find({"word": word})

        print(word_index)

        result = []
        print("Found:")
        print(word_index)
        # for url in word_index:
        # while word_index

        # for url in word_index["urls"]:
        for item in word_index:
            for url in item['urls']:
                result.append(MongoUtils.find_article_by_url(db, url))
        # for url in word_index["urls"]:
        #     result.append(MongoUtils.find_by_url(url))
        return result

    @staticmethod
    def find_all_articles(db):
        return db.articles.find()

    @staticmethod
    def find_all_words(db):
        return db.words.find()
