import json


class FileWriter:
    @staticmethod
    def write_to_file(data):
        with open('crawler-output.json', 'w') as fp:
            json.dump(data, fp)
