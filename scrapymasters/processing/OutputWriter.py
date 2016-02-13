import json


class OutputWriter:
    def __init__(self):
        pass

    @staticmethod
    def write_to_file(data):
        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)

    @staticmethod
    def write_to_mongo(data):
        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)
