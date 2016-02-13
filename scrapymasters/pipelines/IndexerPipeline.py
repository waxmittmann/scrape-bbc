# import cPickle as pickle
import json
from string import punctuation
from scrapymasters.postcrawl.FileWriter import FileWriter

class IndexerPipeline(object):
    def __init__(self):
        self.article_word_index = {}
        self.articles = []

    def process_item(self, article, spider):
        # print("Brocessing " + article)
        body = article['body']
        for word in body.split():
            word = word.strip(punctuation).lower()
            if len(word) != 0:
                url = article['url']
                # Need to clean word (remove punctuation etc)
                if word in self.article_word_index:
                    self.article_word_index[word].append(url)
                else:
                    self.article_word_index[word] = [url]

        self.articles.append(article)
        return article

    def close_spider(self, spider):
        # print("Spider closing, here is index:")
        # for word in self.article_word_index:
        #     articles = self.article_word_index[word]
        #     print(word + " -> " + ', '.join(articles))
        #
        # with open('guardian-index.json', 'w') as fp:
        #     json.dump(self.article_word_index, fp)

        articles_and_index = {
            'articles': self.articles,
            'index': self.article_word_index
        }
        FileWriter.write_to_file(articles_and_index)


        # print("spider.state.items():")
        # print(spider.state.items())
            # with open('guardian-index.json', 'wb') as fp:
            #     pickle.dump(self.article_word_index, fp)
