import os
from typing import List

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from application.port.out.get_documents_content_port import GetDocumentsContentPort
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager

"""
This class is the implementation of the GetDocumentsContentPort interface. It uses the AWSS3Manager to get the documents content.
    Attributes:
        awsS3Manager (AWSS3Manager): The AWSS3Manager to use to get the documents content.
"""
class GetDocumentsContentAWSS3(GetDocumentsContentPort):

    def __init__(self, awsS3Manager: AWSS3Manager):
        self.awsS3Manager = awsS3Manager

    """
    Gets the documents content and returns the response.
    Args:
        documentIds (List[DocumentId]): The documents to get the content.
    Returns:
        List[PlainDocument]: The content of the documents.
    """
    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[PlainDocument]:
        documents = []
        for documentId in documentIds:
            retrievedDocument = self.awsS3Manager.getDocumentContent(documentId.id)
            documents.append(retrievedDocument)
        
        plainDocuments = [document.toPlainDocument() if document is not None else None for document in documents]
        return plainDocuments

