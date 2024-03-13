import os
from typing import List

from domain.document.document_content import DocumentContent
from domain.document.document_filter import DocumentFilter
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.plain_document import PlainDocument
from application.port.out.get_documents_content_port import GetDocumentsContentPort
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager


class GetDocumentsContentAWSS3(GetDocumentsContentPort):

    def __init__(self, awsS3Manager: AWSS3Manager):
        self.awsS3Manager = awsS3Manager

    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[PlainDocument]:
        documents = []
        for documentId in documentIds:
            retrievedDocument = self.awsS3Manager.getDocumentContent(documentId.id)
            documents.append(retrievedDocument)
        
        plainDocuments = [
            PlainDocument(
                DocumentMetadata(
                    id=DocumentId(document.id),
                    type=DocumentType.PDF if document.type.split('.')[1].upper() == "PDF" else DocumentType.DOCX,
                    size=document.size,
                    uploadTime=document.uploadTime
                ),
                DocumentContent(document.content)
            ) if document is not None else None for document in documents]
        return plainDocuments

