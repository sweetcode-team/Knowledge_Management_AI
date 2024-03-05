from typing import List
from application.port.out.delete_documents_port import DeleteDocumentsPort
from domain.document_operation_response import DocumentOperationResponse
from domain.document_id import DocumentId

class DeleteDocuments:
    def __init__(self, delete_documents_port: DeleteDocumentsPort):
        self.outport = delete_documents_port
    
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outport.deleteDocuments(documentsIds)