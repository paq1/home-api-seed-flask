from typing import TypeVar, Generic

from src.models.shared.CanBeDict import CanBeDict

T = TypeVar('T', bound=CanBeDict)


class Entity(Generic[T]):

    def __init__(self, reference: str, value: T, version: int = 0):
        self.reference = reference
        self.value = value
        self.version = version

    def to_dict(self) -> dict:
        return {
            'entityId': self.reference,
            'value': self.value.to_dict(),
            'version': self.version
        }
