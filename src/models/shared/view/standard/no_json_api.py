from typing import Generic, TypeVar

from src.models.shared.can_be_dict import CanBeDict

T = TypeVar('T', bound=CanBeDict)


class NoJsonApi(Generic[T], CanBeDict):
    def __init__(self, model: T):
        self.model = model

    def to_dict(self) -> dict:
        return self.model.to_dict()
