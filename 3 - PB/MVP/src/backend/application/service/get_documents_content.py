from typing import List

from domain.configuration.configuration import Configuration
from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from application.port.out.get_document_content_port import GetDocumentContentsPort


class GetDocumentsContent():
    def __init__(self, outPort: GetDocumentContentsPort):
        self.outPort = outPort

    def getDocumentsContent(self, documentIds: List[DocumentId])->List[PlainDocument]:
        return self.outPort.getDocumentsContent(documentIds)
