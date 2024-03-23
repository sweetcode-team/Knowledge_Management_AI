from unittest.mock import MagicMock, patch
from application.service.embed_documents_service import EmbedDocumentsService
from domain.exception.exception import ElaborationException


def test_embedDocumentsService():
    with    patch('application.service.embed_documents_service.Status') as statusMock, \
            patch('application.service.embed_documents_service.Document') as documentMock:
        embeddingsUploaderPortMock = MagicMock()
        getDocumentsStatusPortMock = MagicMock()
        getDocumentsContentMock = MagicMock()
        documentIdMock = MagicMock()
        documentStatusMock = MagicMock()
        plainDocumentMock = MagicMock()

        getDocumentsStatusPortMock.getDocumentsStatus.return_value = [documentStatusMock]
        documentStatusMock.status = statusMock.NOT_EMBEDDED
        getDocumentsContentMock.getDocumentsContent.return_value = [plainDocumentMock]

        embedDocumentsService = EmbedDocumentsService(getDocumentsContentMock, embeddingsUploaderPortMock, getDocumentsStatusPortMock)

        response = embedDocumentsService.embedDocuments([documentIdMock])
                
        getDocumentsStatusPortMock.getDocumentsStatus.assert_called_once_with([documentIdMock]) 
        getDocumentsContentMock.getDocumentsContent.assert_called_once_with([documentIdMock])
        documentMock.assert_called_once_with(documentStatusMock, plainDocumentMock)
        embeddingsUploaderPortMock.uploadEmbeddings.assert_called_once_with([documentMock.return_value])    
        assert response == embeddingsUploaderPortMock.uploadEmbeddings.return_value
        
def test_embedDocumentsServiceFailGetDocumentStatus():
    with    patch('application.service.embed_documents_service.Status') as statusMock, \
            patch('application.service.embed_documents_service.Document') as documentMock:
        embeddingsUploaderPortMock = MagicMock()
        getDocumentsStatusPortMock = MagicMock()
        getDocumentsContentMock = MagicMock()
        documentIdMock = MagicMock()
        documentStatusMock = MagicMock()
        plainDocumentMock = MagicMock()

        getDocumentsStatusPortMock.getDocumentsStatus.return_value = []
        documentStatusMock.status = statusMock.NOT_EMBEDDED
        getDocumentsContentMock.getDocumentsContent.return_value = [plainDocumentMock]

        embedDocumentsService = EmbedDocumentsService(getDocumentsContentMock, embeddingsUploaderPortMock, getDocumentsStatusPortMock)

        try:
            response = embedDocumentsService.embedDocuments([documentIdMock])
            assert False
        except ElaborationException:
            getDocumentsStatusPortMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
            pass

def test_embedDocumentsServiceFailGetDocumentStatusNotNOT_EMBEDDED():   
    with    patch('application.service.embed_documents_service.Status') as statusMock, \
            patch('application.service.embed_documents_service.Document') as documentMock:
        embeddingsUploaderPortMock = MagicMock()
        getDocumentsStatusPortMock = MagicMock()
        getDocumentsContentMock = MagicMock()
        documentIdMock = MagicMock()
        documentStatusMock = MagicMock()
        plainDocumentMock = MagicMock()

        getDocumentsStatusPortMock.getDocumentsStatus.return_value = [documentStatusMock]
        documentStatusMock.status = statusMock.CONCEAL
        getDocumentsContentMock.getDocumentsContent.return_value = [plainDocumentMock]

        embedDocumentsService = EmbedDocumentsService(getDocumentsContentMock, embeddingsUploaderPortMock, getDocumentsStatusPortMock)

        try:
            response = embedDocumentsService.embedDocuments([documentIdMock])
            assert False
        except ElaborationException:
            getDocumentsStatusPortMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
            pass
     
def test_embedDocumentsServiceFailGetDocumentContent():
    with    patch('application.service.embed_documents_service.Status') as statusMock, \
            patch('application.service.embed_documents_service.Document') as documentMock:
        embeddingsUploaderPortMock = MagicMock()
        getDocumentsStatusPortMock = MagicMock()
        getDocumentsContentMock = MagicMock()
        documentIdMock = MagicMock()
        documentStatusMock = MagicMock()
        plainDocumentMock = MagicMock()

        getDocumentsStatusPortMock.getDocumentsStatus.return_value = [documentStatusMock]
        documentStatusMock.status = statusMock.NOT_EMBEDDED
        getDocumentsContentMock.getDocumentsContent.return_value = []

        embedDocumentsService = EmbedDocumentsService(getDocumentsContentMock, embeddingsUploaderPortMock, getDocumentsStatusPortMock)

        try:
            response = embedDocumentsService.embedDocuments([documentIdMock])
            assert False
        except ElaborationException:
            getDocumentsStatusPortMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
            getDocumentsContentMock.getDocumentsContent.assert_called_once_with([documentIdMock])
            pass