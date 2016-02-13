from string import punctuation
from scrapymasters.processing.OutputWriter import OutputWriter
import urllib
import cgi


class IndexerPipeline(object):
    def __init__(self):
        self.article_word_index = {}
        self.articles = []
        self.outputWriter = OutputWriter()
        self.remove_punctuation_map = dict((ord(char), None) for char in punctuation)

    def process_item(self, article, spider):
        body = article['body']
        for word in body.split():
            # word = urllib.urlencode(word.strip(punctuation).lower())
            # word = cgi.escape(word.strip(punctuation).lower())
            # word = urllib.quote(word.strip(punctuation).lower())

            #remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
            #word_list = [s.translate(remove_punctuation_map) for s in value_list]

            # oldWord = word
            word = word.strip(punctuation).lower()
            # word = word.translate(None, '.')
            # word = [word.translate(self.remove_punctuation_map) for s in value_list]

            # print(oldWord)
            # if oldWord == "71.8%":
            #     print("Conversion: " + word + " = " + oldWord)

            if len(word) != 0 and word.isalpha():
                url = article['url']
                # Need to clean word (remove punctuation etc)
                if word in self.article_word_index:
                    self.article_word_index[word].append(url)
                else:
                    self.article_word_index[word] = [url]

        self.articles.append(article)
        return article

    # This doesn't really seem like a good way to write the output (in a random pipeline stage) but actually doing it
    # as an exporter or something seems harder. Maybe a better alternative would be to add a separate 'final' pipeline
    # stage that does the article-storing, processing and writing.
    def close_spider(self, spider):
        just_articles = {
            'articles': self.articles
        }

        articles_and_index = {
            'articles': self.articles,
            'index': self.article_word_index
        }
        self.outputWriter.write_to_file(articles_and_index)
        self.outputWriter.write_to_mongo(articles_and_index)
        # print("type of articles: ")
        # print(type(self.articles))
        # self.outputWriter.write_to_mongo(just_articles)
