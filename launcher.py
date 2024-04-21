from flask import Flask, jsonify

from src.models.documents.document_details import DocumentDetails
from src.models.documents.views.document_view import DocumentView
from src.models.shared.view.message import message

app = Flask(__name__)


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
