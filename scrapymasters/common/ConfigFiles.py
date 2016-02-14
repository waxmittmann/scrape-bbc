import ConfigParser


class ConfigFiles:
    def __init__(self):
        pass

    @staticmethod
    def config():
        config_file_path = ConfigFiles.config_file()
        config = ConfigParser.ConfigParser()
        config.read("./config/" + config_file_path)
        config = {
            'url': config.get("Mongo", "url"),
            'username': config.get("Mongo", "username"),
            'password': config.get("Mongo", "password"),
            'dbname': config.get("Mongo", "dbname"),
            'scrapeUrl': config.get("Scrape", "url"),
        }
        return config

    @staticmethod
    def config_file():
        config = ConfigParser.ConfigParser()
        config.read("./config/environment.cfg")
        config_file = config.get("Config", "configFile")
        return config_file
