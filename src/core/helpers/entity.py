from typing import TypeVar, Generic

from src.models.shared.can_be_dict import CanBeDict

T = TypeVar('T', bound=CanBeDict)


class Entity(Generic[T]):

    def __init__(self, reference: str, value: T, kind: str, version: int = 0):
        self.reference: str = reference
        self.value: T = value
        self.kind: str = kind
        self.version: int = version

    def to_dict(self) -> dict:
        return {
            'entityId': self.reference,
            'value': self.value.to_dict(),
            'kind': self.kind,
            'version': self.version
        }
