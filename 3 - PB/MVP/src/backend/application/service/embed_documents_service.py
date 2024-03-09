from typing import List
from application.port._in.embed_documents_use_case import EmbedDocumentsUseCase
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.get_documents_content import GetDocumentsContent
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.get_documents_status import GetDocumentsStatus
from domain.document.document_status import Status
from domain.document.document import Document

class EmbedDocumentsService(EmbedDocumentsUseCase):
    def __init__(self, getDocumentsContent: GetDocumentsContent, embeddingsUploader: EmbeddingsUploader, getDocumentStatus: GetDocumentsStatus):
        self.getDocumentsContent = getDocumentsContent
        self.embeddingsUploader = embeddingsUploader
        self.getDocumentStatus = getDocumentStatus

    def embedDocuemnts(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        verifiedDocumentsIds =[]
        verifiedDocumentsStatus = []
        for documentId, documentStatus in zip(documentsIds, self.getDocumentStatus.getDocumentsStatus(documentsIds)):
            if documentStatus.status==Status.NOT_EMBEDDED:
                verifiedDocumentsIds.append(documentId)
                verifiedDocumentsStatus.append(documentStatus)
        
        plainDocuments = self.getDocumentsContent.getDocumentsContent(verifiedDocumentsIds)
        
        documents = []
        for plainDocument, documentStatus in zip(plainDocuments, verifiedDocumentsStatus):
            documents.append(Document(documentStatus, plainDocument))
        
        return self.embeddingsUploader.uploadEmbeddings(documents)