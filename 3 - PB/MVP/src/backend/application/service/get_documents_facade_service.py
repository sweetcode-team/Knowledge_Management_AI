from typing import List

from application.port._in.get_documents_use_case import GetDocumentsUseCase
from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_metadata import GetDocumentsMetadata


class GetDocumentsFacadeService(GetDocumentsUseCase):
    def __init__(self, getDocumentsMetadatas: GetDocumentsMetadata, getDocumentsStatus: GetDocumentsStatus):
        self.getDocumentsMetadatas = getDocumentsMetadatas
        self.getDocumentsStatus = getDocumentsStatus

    def getDocuments(self, documentFilter: DocumentFilter) -> List[LightDocument]:
        documentsMetadataList = self.getDocumentsMetadatas.getDocumentsMetadata(documentFilter)

        documentsId = [document.id for document in documentsMetadataList]
        documentsStatusList = self.getDocumentsStatus.getDocumentsStatus(documentsId)
        if len(documentsMetadataList) != len(documentsStatusList):
            raise Exception("Il numero di documenti e di status non corrisponde.")
        listOfLightDocument = []
        for documentMetadata, documentStatus in zip(documentsMetadataList, documentsStatusList):
            lightdocs = LightDocument(metadata=documentMetadata, status=documentStatus)
            listOfLightDocument.append(lightdocs)
        return listOfLightDocument