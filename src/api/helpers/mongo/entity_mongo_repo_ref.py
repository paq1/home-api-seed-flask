from flask import jsonify
from pymongo import MongoClient
from typing import TypeVar, Generic

from src.core.helpers.entity import Entity

T = TypeVar('T')


class EntityMongoRepoRef(Generic[T]):
    def __init__(self, client: MongoClient, db_name: str, collection_name: str):
        self.db_name = db_name
        self.collection_name = collection_name

        self.database = client[self.db_name]

    def insert_one(self, entity: Entity[T]):
        jsvalue = jsonify(entity.to_dict()).json
        return self.database[self.collection_name].insert_one(document=jsvalue)
