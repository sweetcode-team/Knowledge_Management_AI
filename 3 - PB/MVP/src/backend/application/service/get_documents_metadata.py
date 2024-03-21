from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort

"""
This class is the implementation of the GetDocumentsMetadataUseCase interface.
    Attributes:
        outPort (GetDocumentsMetadataPort): The port to use to get the documents metadata.
"""
class GetDocumentsMetadata:
    def __init__(self, outPort: GetDocumentsMetadataPort):
        self.outPort = outPort
    
    """
    Gets the documents metadata and returns it.
    Args:
        documentFilter (DocumentFilter): The document filter.
    Returns:
        List[DocumentMetadata]: The documents metadata.
    """ 
    def getDocumentsMetadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        return self.outPort.getDocumentsMetadata(documentFilter)
