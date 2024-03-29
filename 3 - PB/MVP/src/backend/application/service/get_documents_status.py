from typing import List, Dict

from application.port.out.get_documents_status_port import GetDocumentsStatusPort
from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus

"""
This class is the implementation of the GetDocumentsStatusUseCase interface.
    Attributes:
        outPort (GetDocumentsStatusPort): The port to use to get the documents status.
"""
class GetDocumentsStatus:
    def __init__(self, outPort: GetDocumentsStatusPort):
        self.outPort = outPort
    
    """
    Gets the documents status and returns it.
    Args:
        documentsIds (List[DocumentId]): The documents ids.
    Returns:
        List[DocumentStatus]: The documents status.
    """ 
    def getDocumentsStatus(self, documentsIds: List[DocumentId]) -> List[DocumentStatus]:
        return self.outPort.getDocumentsStatus(documentsIds)
