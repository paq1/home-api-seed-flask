from src.models.shared.can_be_dict import CanBeDict


class MessageView(CanBeDict):
    def __init__(self, content: str):
        self.content = content

    def to_dict(self) -> dict:
        return {'data': self.content}
