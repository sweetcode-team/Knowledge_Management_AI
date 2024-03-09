from typing import List

from domain.configuration.configuration import Configuration
from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from application.port.out.get_documents_content_port import GetDocumentsContentPort


class GetDocumentsContent:
    def __init__(self, outPort: GetDocumentsContentPort):
        self.outPort = outPort

    def getDocumentsContent(self, documentIds: List[DocumentId])->List[PlainDocument]:
        return self.outPort.getDocumentsContent(documentIds)
