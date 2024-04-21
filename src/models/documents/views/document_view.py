from src.models.documents.document_details import DocumentDetails


class DocumentView:

    def __init__(self, document_details: DocumentDetails):
        self.details = document_details

    def to_map_schema(self) -> dict:
        return {
            "name": self.details.get_name(),
            "category": self.details.get_category(),
        }
