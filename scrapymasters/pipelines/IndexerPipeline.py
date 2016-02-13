# import cPickle as pickle
import json

class IndexerPipeline(object):
    def __init__(self):
        self.article_word_index = {}

    def process_item(self, article, spider):
        body = article['body']
        for word in body.split():
            url = article['url']
            #Need to clean word (remove punctuation etc)
            if word in self.article_word_index:
                self.article_word_index[word].append(url)
            else:
                self.article_word_index[word] = [url]

        return article

    def close_spider(self, spider):
        print("Spider closing, here is index:")
        for word in self.article_word_index:
            articles = self.article_word_index[word]
            print(word + " -> " + ', '.join(articles))

        with open('guardian-index.json', 'w') as fp:
            json.dump(self.article_word_index, fp)

        # with open('guardian-index.json', 'wb') as fp:
        #     pickle.dump(self.article_word_index, fp)
