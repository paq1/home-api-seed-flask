from src.models.documents.document_details import DocumentDetails
from src.models.shared.can_be_dict import CanBeDict


class DocumentView(CanBeDict):

    def __init__(self, document_details: DocumentDetails):
        self.details = document_details

    def to_dict(self) -> dict:
        return {
            "name": self.details.get_name(),
            "category": self.details.get_category(),
        }
