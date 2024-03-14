import os
from typing import List

from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort

"""
This class is the implementation of the GetDocumentsMetadataPort interface. It uses the AWSS3Manager to get the documents metadata.
    Attributes:
        awsS3Manager (AWSS3Manager): The AWSS3Manager to use to get the documents metadata.
"""
class GetDocumentsListAWSS3(GetDocumentsMetadataPort):
    def __init__(self, awsS3Manager: AWSS3Manager):
        self.awsS3Manager = awsS3Manager
    """
    Gets the documents metadata and returns the response.
    Args:
        documentFilter (DocumentFilter): The document filter.
    Returns:
        List[DocumentMetadata]: The metadata of the documents.
    """
    def getDocumentsMetadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        documentsMetadatas = []
        documentsMetadata = self.awsS3Manager.getDocumentsMetadata(documentFilter.searchFilter)
        for documentMetadata in documentsMetadata:
            documentsMetadatas.append(documentMetadata.toDocumentMetadataFrom())
        return documentsMetadatas