from typing import List, Dict

from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus


class GetDocumentsStatusPort:
    def getDocumentsStatus(self, documentsId: List[DocumentId])-> Dict[DocumentId, DocumentStatus]:
        pass