from typing import Generic, TypeVar

from src.models.shared.can_be_dict import CanBeDict
from src.models.shared.view.standard.data_view_api import DataViewApi

T = TypeVar('T', bound=CanBeDict)
ID = TypeVar('ID')


class SingleJsonApi(Generic[T, ID], CanBeDict):
    def __init__(self, data: T, entityId: ID, kind: str):
        self.data = DataViewApi(attributes=data, entityId=entityId, kind=kind)

    def to_dict(self) -> dict:
        return {
            'data': self.data.to_dict(),
        }
