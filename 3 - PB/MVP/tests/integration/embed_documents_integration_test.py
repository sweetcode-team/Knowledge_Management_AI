from unittest.mock import MagicMock, patch
from application.service.embed_documents_service import EmbedDocumentsService
from application.service.get_documents_content import GetDocumentsContent
from application.service.get_documents_status import GetDocumentsStatus
from application.service.embeddings_uploader import EmbeddingsUploader

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_content import DocumentContent
from domain.document.document_status import DocumentStatus, Status
from domain.document.document_operation_response import DocumentOperationResponse

from datetime import datetime

def test_embedDocumentsBusiness():
    getDocumentsContentPortMock = MagicMock()
    getDocumentsContentPortMock.getDocumentsContent.return_value = [PlainDocument(
        DocumentMetadata(
            DocumentId("Prova.pdf"),
            DocumentType.PDF,
            10,
            datetime(2021, 1, 1, 1, 1, 1),
        ),
        DocumentContent(b'content')
    )]
    
    getDocumentsStatusPortMock = MagicMock()
    getDocumentsStatusPortMock.getDocumentsStatus.return_value = [DocumentStatus(Status.NOT_EMBEDDED)]
    
    embeddingsUploaderPortMock = MagicMock()
    embeddingsUploaderPortMock.uploadEmbeddings.return_value = [DocumentOperationResponse(
        DocumentId("Prova.pdf"),
        True, 
        'Embedding completed'
    )]
    
    embedDocumentsService = EmbedDocumentsService(
        GetDocumentsContent(getDocumentsContentPortMock),
        EmbeddingsUploader(embeddingsUploaderPortMock),
        GetDocumentsStatus(getDocumentsStatusPortMock)
    )
    
    response = embedDocumentsService.embedDocuments([DocumentId("Prova.pdf")])
    
    assert response == [DocumentOperationResponse(
        DocumentId("Prova.pdf"),
        True, 
        'Embedding completed'
    )]