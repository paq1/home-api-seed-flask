from typing import Generic, TypeVar

from src.models.shared.can_be_dict import CanBeDict

T = TypeVar('T', bound=CanBeDict)
ID = TypeVar('ID')


class DataViewApi(Generic[T, ID], CanBeDict):
    def __init__(self, attributes: T, entityId: ID, kind: str):
        self.attributes = attributes
        self.entityId = str(entityId)
        self.type = kind

    def to_dict(self) -> dict:
        return {
            'attributes': self.attributes.to_dict(),
            'id': self.entityId,
            'type': self.type
        }
