from flask import Flask, request, jsonify

from src.api.documents.dbo.document_dbo import DocumentDBO
import uuid

from src.api.documents.repository_documents_mongo import RepositoryDocumentsMongo
from src.api.helpers.mongo.mongo_component import MongoComponent
from src.core.helpers.entity import Entity
from src.models.shared.view.message import message


class DocumentWriteComponent:
    def __init__(self, app: Flask, mongo_component: MongoComponent):
        self.app = app
        self.repository_documents_mongo = RepositoryDocumentsMongo(mongo_component.client_mongo)
        self.__initialize_routes()

    def __initialize_routes(self):
        @self.app.route('/documents/commands/create', methods=['POST'])
        def insert_doc():  # put application's code here

            request_json = request.get_json()
            name: str = request_json["name"]
            document: DocumentDBO = DocumentDBO(name)
            entity_id = str(uuid.uuid4())

            entity: Entity[DocumentDBO] = Entity(entity_id, document)

            result = self.repository_documents_mongo.insert_one(entity)
            return jsonify(message(f"inserted {result.inserted_id}")), 201
