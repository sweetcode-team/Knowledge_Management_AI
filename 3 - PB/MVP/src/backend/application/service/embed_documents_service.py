from typing import List
from application.port._in.embed_documents_use_case import EmbedDocumentsUseCase
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.get_documents_content import GetDocumentsContent
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.get_documents_status import GetDocumentsStatus
from domain.document.document_status import Status
from domain.document.document import Document

from domain.exception.exception import ElaborationException
"""
This class is the implementation of the EmbedDocumentsUseCase interface.
    Attributes:
        getDocumentsContent (GetDocumentsContent): The port to use to get the documents content.
        embeddingsUploader (EmbeddingsUploader): The port to use to upload the documents embeddings.
        getDocumentStatus (GetDocumentsStatus): The port to use to get the documents status.
"""
class EmbedDocumentsService(EmbedDocumentsUseCase):
    def __init__(self, getDocumentsContent: GetDocumentsContent, embeddingsUploader: EmbeddingsUploader, getDocumentStatus: GetDocumentsStatus):
        self.getDocumentsContent = getDocumentsContent
        self.embeddingsUploader = embeddingsUploader
        self.getDocumentStatus = getDocumentStatus

    
    """
    Embeds the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to embed.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def embedDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        verifiedDocumentsIds =[]
        verifiedDocumentsStatus = []
        
        documentsStatus = self.getDocumentStatus.getDocumentsStatus(documentsIds)
        
        if len(documentsIds) != len(documentsStatus) or len(documentsStatus) == 0:
            raise ElaborationException("Errore nel recupero degli stati dei documenti.")
        
        for documentId, documentStatus in zip(documentsIds, documentsStatus):
            if documentStatus.status == Status.NOT_EMBEDDED:
                verifiedDocumentsIds.append(documentId)
                verifiedDocumentsStatus.append(documentStatus)
        
        plainDocuments = self.getDocumentsContent.getDocumentsContent(verifiedDocumentsIds)
        
        if len(verifiedDocumentsIds) != len(plainDocuments) or len(plainDocuments) == 0:
            raise ElaborationException("Errore nel recupero dei contenuti dei documenti.")
        
        documentsToEmbed = []
        for plainDocument, documentStatus in zip(plainDocuments, verifiedDocumentsStatus):
            documentsToEmbed.append(Document(documentStatus, plainDocument)) if plainDocument else None
        
        if len(documentsToEmbed) != len(verifiedDocumentsStatus):
            raise ElaborationException("Errore nel recupero dei contenuti dei documenti.")
        return self.embeddingsUploader.uploadEmbeddings(documentsToEmbed)