from flask import Flask, jsonify

from src.models.documents.document_details import DocumentDetails
from src.models.documents.views.document_view import DocumentView
from src.models.shared.view.message_view import MessageView
from src.models.shared.view.standard.no_json_api import NoJsonApi


class DocumentReadComponent:
    def __init__(self, app: Flask):
        self.app = app
        self.__initialize_routes()

    def __initialize_routes(self):
        @self.app.route('/health')
        def get_health():  # put application's code here
            return jsonify(NoJsonApi(MessageView("up")).to_dict()), 200

        @self.app.route('/get-document-infos/<string:user>/<string:entity_id>', methods=['GET'])
        def get_documents(user: str, entity_id: str):  # put application's code here
            document_detail = DocumentDetails(entity_id, "category")
            view = DocumentView(document_detail)
            return jsonify(view.to_dict()), 200
