from pymongo import MongoClient


class MongoComponent:
    def __init__(self):
        # fixme mettre ca dans les variables environments
        uri = 'mongodb://localhost:27017/'
        self.client_mongo = MongoClient(uri)

    def close_connection(self):
        return self.client_mongo.close()
