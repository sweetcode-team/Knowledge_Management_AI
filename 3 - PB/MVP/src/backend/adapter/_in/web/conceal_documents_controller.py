from typing import List
from application.port._in.conceal_documents_use_case import ConcealDocumentsUseCase
#from .configuration_service import ConfigurationService
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

class ConcealDocumentsController:
    def __init__(self, concealDocumentsUseCase: ConcealDocumentsUseCase): #configurationService: ConfigurationService
        self.useCase = concealDocumentsUseCase 
        #self.configurationService = configurationService
        
    def concealDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:        
        return self.useCase.concealDocuments([DocumentId(documentId) for documentId in documentsIds])