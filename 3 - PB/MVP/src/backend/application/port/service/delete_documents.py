from typing import List
from application.port.out.delete_documents_port import DeleteDocumentsPort
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

class DeleteDocuments:
    def __init__(self, deleteDocumentsPort: DeleteDocumentsPort):
        self.outport = deleteDocumentsPort
    
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outport.deleteDocuments(documentsIds)