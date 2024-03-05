from typing import List

from adapter.out.persistence.AWS_document import AWSDocument
from adapter.out.persistence.AWS_manager import AWSS3Manager
from application.port.out.document_uploader_port import DocumentUploaderPort
from domain.document import Document
from domain.document_id import DocumentId
from domain.document_operation_response import DocumentOperationResponse

"""
    A documents uploader that uploads documents to the AWS S3 bucket.
Attributes:
    awss3manager (AWSS3Manager): The AWS S3 manager.
Methods:
    uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]: 
        Uploads a list of documents to the AWS S3 bucket.
    toAWSDocumentFrom(self, document: Document) -> AWSDocument:
        Converts a document to an AWS document.
"""
class DocumentsUploaderAWSS3(DocumentUploaderPort):
    def __init__(self, awss3manager: AWSS3Manager):
        self.awss3manager = awss3manager
    """
        Uploads a list of documents to the AWS S3 bucket.
    Args:
        documents (List[Document]): The list of documents to upload.
        forceUpload (bool): A flag indicating whether to force the upload of the documents, even if they already exist in the bucket.
    Attributes:
        awss3manager (AWSS3Manager): The AWS S3 manager.
    Returns:
        List[DocumentOperationResponse]: A list of document operation responses.
    """
    def uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]:
        #adaptee because awss3manager needs a ListOfAWSDocument
        awsDocuments = [self.toAWSDocumentFrom(document) for document in documents]
        awsDocumentOperationResponseList = self.awss3manager.uploadDocuments(awsDocuments, forceUpload)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for awsDocumentOperationResponse in awsDocumentOperationResponseList:
            documentOperationResponseList.append(awsDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList

    """
        Converts a document to an AWS document.
    Args:
        document (Document): The document to convert.
    Returns:
        AWSDocument: The AWS document.
    """
    def toAWSDocumentFrom(self, document: Document) -> AWSDocument:
        #TODO guardare type cosa ritorna e se è corretto
        return AWSDocument(id=document.plainDocument.metadata.id.id,
                           content=document.plainDocument.content.content,
                           type=str(document.plainDocument.metadata.type),
                           size=document.plainDocument.metadata.size,
                           uploadTime=document.plainDocument.metadata.uploadTime)