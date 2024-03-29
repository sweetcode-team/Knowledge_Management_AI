from typing import List

from domain.configuration.configuration import Configuration
from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from application.port.out.get_documents_content_port import GetDocumentsContentPort

"""
This class is the implementation of the GetDocumentsContentUseCase interface.
    Attributes:
        outPort (GetDocumentsContentPort): The port to use to get the documents content.
"""
class GetDocumentsContent:
    def __init__(self, outPort: GetDocumentsContentPort):
        self.outPort = outPort
    
    """
    Gets the documents content and returns it.
    Args:
        documentIds (List[DocumentId]): The documents ids.
    Returns:
        List[PlainDocument]: The documents content.
    """ 
    def getDocumentsContent(self, documentIds: List[DocumentId])->List[PlainDocument]:
        return self.outPort.getDocumentsContent(documentIds)
