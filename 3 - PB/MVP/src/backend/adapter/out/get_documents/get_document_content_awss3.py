import os
from typing import List

from domain.document.document_content import DocumentContent
from domain.document.document_filter import DocumentFilter
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.plain_document import PlainDocument
from application.port.out.get_document_content_port import GetDocumentContentsPort
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager


class GetDocumentContentsAWSS3(GetDocumentContentsPort):

    def __init__(self, awsS3Manager: AWSS3Manager):
        self.awsS3Manager = awsS3Manager

    def getDocumentsContent(self, documentsId: List[DocumentId]) -> List[PlainDocument]:
        documents = []
        for documentId in documentsId:
            document = self.awsS3Manager.getDocumentContent(documentId.id)
            documents.append(document)
        listOfPlainDocuments = [PlainDocument(DocumentMetadata(id= DocumentId(doc.id),
                                                               type= DocumentType.PDF if os.path.splitext(doc.type)[1].upper() == ".PDF" else DocumentType.DOCX,
                                                               size=doc.size,
                                                               uploadTime=doc.uploadTime),
                                              DocumentContent(doc.content)) for doc in documents]
        return listOfPlainDocuments

