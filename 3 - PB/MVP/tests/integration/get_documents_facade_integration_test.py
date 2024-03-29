from unittest.mock import MagicMock, patch

from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus, Status
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.light_document import LightDocument
from domain.document.document_filter import DocumentFilter

from application.service.get_documents_facade_service import GetDocumentsFacadeService
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_metadata import GetDocumentsMetadata


from datetime import datetime

def test_getDocumentsFacadeBusiness():
    getDocumentsMetadataPortMock = MagicMock()
    getDocumentsMetadataPortMock.getDocumentsMetadata.return_value = [
        DocumentMetadata(
            DocumentId("Prova.pdf"),
            DocumentType.PDF,
            10,
            datetime(2021, 1, 1, 1, 1, 1),
        )]
    
    getDocumentsStatusPortMock = MagicMock()
    getDocumentsStatusPortMock.getDocumentsStatus.return_value = [DocumentStatus(Status.ENABLED)]
    
    getDocumentsFacadeService = GetDocumentsFacadeService(
        GetDocumentsMetadata(getDocumentsMetadataPortMock),
        GetDocumentsStatus(getDocumentsStatusPortMock)
    )
    
    response = getDocumentsFacadeService.getDocuments(DocumentFilter(""))
    
    assert response == [LightDocument(
        status=DocumentStatus(Status.ENABLED),
        metadata=DocumentMetadata(
            DocumentId("Prova.pdf"),
            DocumentType.PDF,
            10,
            datetime(2021, 1, 1, 1, 1, 1),
        )
    )]