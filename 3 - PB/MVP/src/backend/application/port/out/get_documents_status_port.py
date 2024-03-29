from typing import List, Dict

from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus

"""
This interface is the output port of the GetDocumentsStatusUseCase. It is used to get the documents status.
"""
class GetDocumentsStatusPort:
       
    """
    Gets the documents status and returns the document status.
    Args:
        documentsId (List[DocumentId]): The document ids.
    Returns:
        List[DocumentStatus]: The document status.
    """ 
    def getDocumentsStatus(self, documentsId: List[DocumentId])-> List[DocumentStatus]:
        pass