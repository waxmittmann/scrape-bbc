#!/usr/bin/env python
import web
from pymongo import MongoClient
from scrapymasters.common.ConfigFiles import ConfigFiles

urls = (
    '/articles', 'Articles'
    # '/users/(.*)', 'get_user'
)

# def run(self, port=8080, *middleware):
#         func = self.wsgifunc(*middleware)
#         return web.httpserver.runsimple(func, ('0.0.0.0', port))

app = web.application(urls, globals())


class Articles:
    def __init__(self):
        self.config = ConfigFiles.config

    def GET(self):
        config = self.config
        if config.username == "" and config.password == "":
            client = MongoClient("mongodb://" + config.url + "/" + config.dbname)
        else:
            client = MongoClient("mongodb://" + config.username + ":" + config.password + "@" + config.url + "/" + config.dbname)
        db = client.scrape
        articles = db.articles.find()
        client.close()
        return articles
        # return "getting articles"

    def PUT(self):
        return "putting articles"

# class get_user:
#     def GET(self, user):
# 	for child in root:
# 		if child.attrib['id'] == user:
# 		    return str(child.attrib)

if __name__ == "__main__":
    app.run()
