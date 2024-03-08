from typing import List, Dict

from application.port.out.get_documents_status_port import GetDocumentsStatusPort
from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus


class GetDocumentsStatus:
    def __init__(self, outPort: GetDocumentsStatusPort):
        self.outPort = outPort

    def getDocumentsStatus(self, documentsIds: List[DocumentId]) -> Dict[DocumentId, DocumentStatus]:
        return self.outPort.getDocumentsStatus(documentsIds)
