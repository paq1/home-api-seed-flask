from flask import Flask

from src.api.documents.document_read_component import DocumentReadComponent
from src.api.documents.document_write_component import DocumentWriteComponent
from src.api.helpers.mongo.mongo_component import MongoComponent


class MainComponent:
    def __init__(self):
        self.app: Flask = Flask(__name__)
        self.mongo_component: MongoComponent = MongoComponent()
        self.document_write_component = DocumentWriteComponent(self.app, self.mongo_component)
        self.document_read_component = DocumentReadComponent(self.app)

    def start_server(self):
        self.app.run()

    def delete(self):
        self.mongo_component.client_mongo.close()
