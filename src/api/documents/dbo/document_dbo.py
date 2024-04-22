from src.models.shared.can_be_dict import CanBeDict


class DocumentDBO(CanBeDict):
    def __init__(self, name: str):
        self.name = name

    def to_dict(self) -> dict:
        return {
            'name': self.name
        }
