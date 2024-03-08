from application.port._in.get_document_content_use_case import GetDocumentContentUseCase
from domain.document.document import Document
from domain.document.document_id import DocumentId


class GetDocumentContentController:
    def __init__(self, getDocumentContentUseCase: GetDocumentContentUseCase):
        self.useCase = getDocumentContentUseCase

    def getDocumentContent(self, documentId: str) -> Document:
        prova = self.useCase.getDocumentContent(DocumentId(documentId))
        print(prova, flush=True)
        return prova[0]
