from application.port._in.conceal_documents_use_case import ConcealDocumentsUseCase
from domain.document.document_id import DocumentId
from typing import List
from domain.document.document_operation_response import DocumentOperationResponse
from application.port.out.conceal_documents_port import ConcealDocumentsPort

"""
This class is the implementation of the ConcealDocumentsUseCase interface.
    Attributes:
        outPort (ConcealDocumentsPort): The port to use to conceal the documents.
"""
class ConcealDocumentsService(ConcealDocumentsUseCase):
    def __init__(self, concealDocumentsPort: ConcealDocumentsPort):
        self.outPort = concealDocumentsPort
           
              
    """
    Conceals the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to conceal.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def concealDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outPort.concealDocuments(documentsIds)
    
