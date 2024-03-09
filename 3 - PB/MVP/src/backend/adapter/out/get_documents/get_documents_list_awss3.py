import os
from typing import List

from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from domain.document.document_filter import DocumentFilter
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from adapter.out.persistence.aws.AWS_document_metadata import AWSDocumentMetadata
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort


class GetDocumentsListAWSS3(GetDocumentsMetadataPort):
    def __init__(self, awsS3Manager: AWSS3Manager):
        self.awsS3Manager = awsS3Manager

    def getDocumentsMetadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        listOfDocumentsMetadata = []
        documentsMetadatas = self.awsS3Manager.getDocumentsMetadata(documentFilter.searchFilter)
        for documentMetadata in documentsMetadatas:
            documentM = documentMetadata.toDocumentMetadataFrom()
            listOfDocumentsMetadata.append(documentM)
        return listOfDocumentsMetadata