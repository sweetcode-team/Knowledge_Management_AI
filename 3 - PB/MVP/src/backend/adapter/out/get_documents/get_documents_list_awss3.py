from typing import List

from adapter.out.persistence.aws import AWS_manager
from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata
from adapter.out.persistence.aws.AWS_document_metadata import AWSDocumentMetadata
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort


class GetDocumentsListAWSS3(GetDocumentsMetadataPort):
    def __init__(self, awsS3Manager: AWS_manager):
        self.awsS3Manager = awsS3Manager

    #TODO implement this method
    def get_documents_metadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        listOfDocumentsMetadata = []
        documentsMetadatas =  self.awsS3Manager.getDocumentsMetadata(documentFilter.searchFilter)
        #for documentMetadata in documentsMetadatas:
        #    documentM = GetDocumentsListAWSS3.toDocumentMetadataFrom(documentMetadata)
        #    listOfDocumentsMetadata.append(documentM)
        return listOfDocumentsMetadata

    #TODO implement this method
    def toDocumentMetadataFrom( self,  document: AWSDocumentMetadata) -> DocumentMetadata:
        pass
