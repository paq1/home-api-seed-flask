from flask import Flask, jsonify, request

from src.api.documents.dbo.document_dbo import DocumentDBO
from src.api.documents.repository_documents_mongo import RepositoryDocumentsMongo
from src.api.helpers.mongo.mongo_component import MongoComponent
from src.core.helpers.entity import Entity
from src.models.documents.document_details import DocumentDetails
from src.models.documents.views.document_view import DocumentView
from src.models.shared.view.message import message
import uuid

app = Flask(__name__)

mongo_component = MongoComponent()
repo = RepositoryDocumentsMongo(mongo_component.client_mongo)


@app.route('/documents/commands/create', methods=['POST'])
def insert_doc():  # put application's code here

    request_json = request.get_json()
    name: str = request_json["name"]
    document: DocumentDBO = DocumentDBO(name)
    entity_id = str(uuid.uuid4())

    entity: Entity[DocumentDBO] = Entity(entity_id, document)

    result = repo.insert_one(entity)
    return jsonify(message(f"inserted {result.inserted_id}")), 201


@app.route('/health', methods=['GET'])
def get_health():  # put application's code here

    return jsonify(message("up")), 200


@app.route('/get-document-infos/<string:user>/<string:entity_id>', methods=['GET'])
def get_documents(user: str, entity_id: str):  # put application's code here
    document_detail = DocumentDetails(entity_id, "category")
    view = DocumentView(document_detail)

    return jsonify(view.to_map_schema()), 200


if __name__ == '__main__':
    app.run()
    print("ici")
    mongo_component.close_connection()
