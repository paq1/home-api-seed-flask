from pymongo import MongoClient

from src.api.documents.dbo.document_dbo import DocumentDBO
from src.api.helpers.mongo.entity_mongo_repo_ref import EntityMongoRepoRef


class RepositoryDocumentsMongo(EntityMongoRepoRef[DocumentDBO]):

    def __init__(self, client: MongoClient):
        EntityMongoRepoRef.__init__(self, client, "documents", "documents")
