from typing import List

import embeddings_uploader_port
from domain.document import Document
from domain.document_id import DocumentId
from domain.document_operation_response import DocumentOperationResponse
from embeddings_uploader_port import EmbeddingsUploaderPort

"""
    An embeddings uploader that uploads embeddings to the system.
Methods:
    uploadEmbeddings(self, documents:List[Document]) -> List[DocumentOperationResponse]: 
        Uploads a list of embeddings to the system.
"""


class Configuration:
    pass


class EmbeddingsUploader:
    def __init__(self, outPort:EmbeddingsUploaderPort):
        self.outPort = outPort

    def uploadEmbeddings(self, documents:List[Document], configuration:Configuration) -> List[DocumentOperationResponse]:
        pass
