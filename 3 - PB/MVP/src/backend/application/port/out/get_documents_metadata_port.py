from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata

"""
This interface is the output port of the GetDocumentsMetadataUseCase. It is used to get the documents metadata.
"""
class GetDocumentsMetadataPort:
       
    """
    Gets the documents metadata and returns the document metadata.
    Args:
        documentFilter (DocumentFilter): The document filter.
    Returns:
        List[DocumentMetadata]: The document metadata.
    """ 
    def getDocumentsMetadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        pass