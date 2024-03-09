from application.port._in.get_documents_content_use_case import GetDocumentsContentUseCase
from domain.document.document import Document
from domain.document.document_id import DocumentId


class GetDocumentContentController:
    def __init__(self, getDocumentContentUseCase: GetDocumentsContentUseCase):
        self.useCase = getDocumentContentUseCase

    def getDocumentContent(self, documentId: str) -> Document:
        document = self.useCase.getDocumentsContent([DocumentId(documentId)])
        return document[0]
