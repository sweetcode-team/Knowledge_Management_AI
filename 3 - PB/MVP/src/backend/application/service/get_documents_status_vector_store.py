from typing import List, Dict

from application.port.out.get_documents_status_port import GetDocumentsStatusPort
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus


class GetDocumentsStatusVectorStore(GetDocumentsStatusPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

    def getDocumentsStatus(self, documentsIds: List[DocumentId]) -> Dict[DocumentId, DocumentStatus]:
        listOfDocumentId = []
        for documentId in documentsIds:
            listOfDocumentId.append(documentId.id)
        return self.vectorStoreManager.getDocumentsStatus(listOfDocumentId)
