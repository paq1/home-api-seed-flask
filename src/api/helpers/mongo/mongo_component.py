from pymongo import MongoClient

from src.api.app.configuration import Configuration


class MongoComponent:
    def __init__(self, configuration: Configuration):
        # fixme mettre ca dans les variables environments
        uri: str = configuration.config['mongo']['uri']
        print(f"loading de mongo : {uri}")
        self.client_mongo = MongoClient(uri)

    def close_connection(self):
        return self.client_mongo.close()
