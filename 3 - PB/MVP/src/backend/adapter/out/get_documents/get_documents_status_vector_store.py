from typing import List, Dict

from application.port.out.get_documents_status_port import GetDocumentsStatusPort
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus, Status


class GetDocumentsStatusVectorStore(GetDocumentsStatusPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

    def getDocumentsStatus(self, documentsIds: List[DocumentId]) -> List[DocumentStatus]:
        documentsStatus = []
        statusResponses = self.vectorStoreManager.getDocumentsStatus(documentId.id for documentId in documentsIds)
        for statusResponse in statusResponses:
            if statusResponse.status.upper() == "CONCEALED":
                documentStatus = DocumentStatus(status=Status.CONCEALED)
            elif statusResponse.status.upper() == "ENABLED":
                documentStatus = DocumentStatus(Status.ENABLED)
            elif statusResponse.status.upper() == "INCONSISTENT":
                documentStatus = DocumentStatus(Status.INCONSISTENT)
            else:
                documentStatus = DocumentStatus(Status.NOT_EMBEDDED)
            documentsStatus.append(documentStatus)
        return documentsStatus

