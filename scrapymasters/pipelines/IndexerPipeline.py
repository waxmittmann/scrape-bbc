from string import punctuation
from scrapymasters.processing.FileWriter import FileWriter


class IndexerPipeline(object):
    def __init__(self):
        self.article_word_index = {}
        self.articles = []

    def process_item(self, article, spider):
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

    # This doesn't really seem like a good way to write the output (in a random pipeline stage) but actually doing it
    # as an exporter or something seems harder. Maybe a better alternative would be to add a separate 'final' pipeline
    # stage that does the article-storing, processing and writing.
    def close_spider(self, spider):
        articles_and_index = {
            'articles': self.articles,
            'index': self.article_word_index
        }
        FileWriter.write_to_file(articles_and_index)
