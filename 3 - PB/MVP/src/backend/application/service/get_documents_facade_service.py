from typing import List

from application.port._in.get_documents_use_case import GetDocumentsUseCase
from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument
from application.service.get_document_status import GetDocumentsStatus
from application.service.get_documents_metadata import GetDocumentsMetadata


class GetDocumentsFacadeService(GetDocumentsUseCase):
    def __init__(self, getDocumentsMetadatas: GetDocumentsMetadata):
        self.getDocumentsMetadatas = getDocumentsMetadatas

    def getDocuments(self, documentFilter: DocumentFilter) -> List[LightDocument]:
        documentsMetadataList = self.getDocumentsMetadatas.getDocumentsMetadata(documentFilter)
        #self.getDocumentsStatus.getDocumentsStatus(documentsId)
