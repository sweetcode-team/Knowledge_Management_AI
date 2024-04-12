from typing import List

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument

"""
This interface is the output port of the GetDocumentsContentUseCase. It is used to get the documents content.
"""
class GetDocumentsContentPort:
       
    """
    Gets the documents content and returns the plain documents.
    Args:
        documentIds (List[DocumentId]): The document ids.
    Returns:
        List[PlainDocument]: The plain documents.
    """ 
    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[PlainDocument]:
        pass