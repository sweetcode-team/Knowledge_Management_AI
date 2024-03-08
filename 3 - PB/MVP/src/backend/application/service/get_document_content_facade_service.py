from typing import List

from application.port._in.get_document_content_use_case import GetDocumentContentUseCase
from domain.document.document import Document
from domain.document.document_id import DocumentId
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_content import GetDocumentsContent


class GetDocumentContentFacadeService(GetDocumentContentUseCase):
    def __init__(self, documentContentGetter: GetDocumentsContent, getDocumentsStatus: GetDocumentsStatus):
        self.documentContentGetter = documentContentGetter
        self.getDocumentsStatus = getDocumentsStatus

    def getDocumentContent(self, documentId: DocumentId) -> List[Document]:
        documentContentList = self.documentContentGetter.getDocumentsContent([documentId])
        documentsId = [doc.metadata.id for doc in documentContentList]
        documentsStatusList = self.getDocumentsStatus.getDocumentsStatus(documentsId)
        listOfDocument = []
        for documentContent, documentStatus in zip(documentContentList, documentsStatusList):
            document = Document(plainDocument=documentContent, documentStatus=documentStatus)
            listOfDocument.append(document)
        return listOfDocument
