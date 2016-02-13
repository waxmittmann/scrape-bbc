import json

class FileWriter:
    @staticmethod
    def write_to_file(data):
        # print("Spider closing, here is index:")
        # for word in self.article_word_index:
        #     articles = self.article_word_index[word]
        #     print(word + " -> " + ', '.join(articles))

        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)

            # with open('guardian-index.json', 'wb') as fp:
            #     pickle.dump(self.article_word_index, fp)
