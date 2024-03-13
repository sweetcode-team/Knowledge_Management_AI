from typing import List

from application.port._in.get_documents_use_case import GetDocumentsUseCase
from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_metadata import GetDocumentsMetadata
from domain.exception.exception import ElaborationException


class GetDocumentsFacadeService(GetDocumentsUseCase):
    def __init__(self, getDocumentsMetadatas: GetDocumentsMetadata, getDocumentsStatus: GetDocumentsStatus):
        self.getDocumentsMetadatas = getDocumentsMetadatas
        self.getDocumentsStatus = getDocumentsStatus

    def getDocuments(self, documentFilter: DocumentFilter) -> List[LightDocument]:
        documentsMetadata = self.getDocumentsMetadatas.getDocumentsMetadata(documentFilter)

        documentsId = [document.id for document in documentsMetadata]
        documentsStatus = self.getDocumentsStatus.getDocumentsStatus(documentsId)
        
        if len(documentsMetadata) != len(documentsStatus):
            raise ElaborationException("Errore nel recupero dei documenti.")
        
        lightDocuments = []
        for documentMetadata, documentStatus in zip(documentsMetadata, documentsStatus):
            lightDocument = LightDocument(metadata=documentMetadata, status=documentStatus)
            lightDocuments.append(lightDocument)
        return lightDocuments