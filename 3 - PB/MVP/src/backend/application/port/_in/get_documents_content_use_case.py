from typing import List

from domain.document.document import Document
from domain.document.document_id import DocumentId

"""
This interface is the input port of the GetDocumentsContentUseCase. It is used to get the content of the documents.
"""
class GetDocumentsContentUseCase:
       
    """
    Gets the content of the documents and returns the documents.
    Args:
        documentIds (List[DocumentId]): The documents to get the content.
    Returns:
        List[Document]: The documents with the content.
    """ 
    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[Document]:
        pass