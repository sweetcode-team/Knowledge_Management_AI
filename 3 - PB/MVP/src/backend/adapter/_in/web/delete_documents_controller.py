from application.port._in.delete_documents_use_case import DeleteDocumentsUseCase
#from .configuration_service import ConfigurationService
from domain.document_operation_response import DocumentOperationResponse
from typing import List

from domain.document_id import DocumentId

class DeleteDocumentsController:
    def __init__(self, deleteDocumentsUseCase: DeleteDocumentsUseCase): #configurationService: ConfigurationService
        self.useCase = deleteDocumentsUseCase 
        #self.configurationService = configurationService
        
    def deleteDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:        
        return self.useCase.deleteDocuments([DocumentId(documentId) for documentId in documentsIds])