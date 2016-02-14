import ConfigParser


class ConfigFiles:
    def __init__(self):
        pass

    @staticmethod
    def config():
        config = ConfigParser.ConfigParser()
        config.read("local_config.cfg")
        # config.read("config.cfg")

        config = {
            'url': config.get("Mongo", "url"),
            'username': config.get("Mongo", "username"),
            'password': config.get("Mongo", "password"),
            'dbname': config.get("Mongo", "dbname")
        }
        return config
