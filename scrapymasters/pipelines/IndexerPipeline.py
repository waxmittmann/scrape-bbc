import json
import cPickle as pickle
from pprint import pprint


class IndexerPipeline(object):
    # vat_factor = 1.15

    def __init__(self):
        self.article_word_index = {}

    def process_item(self, article, spider):
        print("Item is:")
        print(article)

        body = article['body']
        print("Body is: " + body)
        for word in body.split():
            url = article['url']
            #Need to clean word (remove punctuation etc)
            if word in self.article_word_index:
                # print("Appending " + word)
                self.article_word_index[word].append(url)
            else:
                # print("Creating new key with " + word)
                self.article_word_index[word] = [url]

        return article
        # item_with_index = {
        #     'articles': item,
        #     'index': self.article_word_index}
        #
        # return item_with_index
        # print(item)
        # with open('guardian-articles.json') as data_file:
        # articles = json.load(data_file)

        # for article in item:
        #     print("Processing: ")
        #     print(article)
        #
        #     if type(article) is list:
        #         for i in article:
        #             yield i
        #     else:
        #         yield article
            # print("Processing ")
            # print(article)
            # yield article

    def close_spider(self, spider):
        print("Spider closing, here is index:")
        for word in self.article_word_index:
            articles = self.article_word_index[word]
            print(word + " -> " + ', '.join(articles))
        with open('guardian-index.json', 'wb') as fp:
            pickle.dump(self.article_word_index, fp)
