from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument

"""
This interface is the input port of the GetDocumentsUseCase. It is used to get the documents.
"""
class GetDocumentsUseCase:
       
    """
    Gets the documents and returns the light documents.
    Args:
        documentFilter (DocumentFilter): The document filter.
    Returns:
        List[LightDocument]: The light documents.
    """ 
    def getDocuments(self, documentFilter: DocumentFilter) -> List[LightDocument]:
        pass