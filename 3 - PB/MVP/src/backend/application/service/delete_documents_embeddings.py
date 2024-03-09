from typing import List
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

class DeleteDocumentsEmbeddings:
    def __init__(self, deleteEmbeddingsPort: DeleteEmbeddingsPort):
        self.outPort = deleteEmbeddingsPort
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outPort.deleteDocumentsEmbeddings(documentsIds)