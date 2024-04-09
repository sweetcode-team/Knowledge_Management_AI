from unittest.mock import MagicMock, patch
from application.service.get_documents_facade_service import GetDocumentsFacadeService
from domain.exception.exception import ElaborationException

def test_getDocumentsFacadeService():
    getDocumentsMetadataMock = MagicMock()
    getDocumentsStatusMock = MagicMock()
    documentFilterMock = MagicMock()
    documentMetadataMock = MagicMock()
    documentStatusMock = MagicMock()
    
    with patch('application.service.get_documents_facade_service.LightDocument') as LightDocumentMock:
        getDocumentsFacadeService = GetDocumentsFacadeService(getDocumentsMetadataMock, getDocumentsStatusMock)
        
        getDocumentsMetadataMock.getDocumentsMetadata.return_value = [documentMetadataMock]
        getDocumentsStatusMock.getDocumentsStatus.return_value = [documentStatusMock]
        
        response = getDocumentsFacadeService.getDocuments(documentFilterMock)
            
        getDocumentsMetadataMock.getDocumentsMetadata.assert_called_once_with(documentFilterMock)
        getDocumentsStatusMock.getDocumentsStatus.assert_called_once_with([documentMetadataMock.id])
        LightDocumentMock.assert_called_once_with(metadata=documentMetadataMock, status=documentStatusMock)
        assert response == [LightDocumentMock.return_value]
        
def test_getDocumentsFacadeServiceFailGetMetadata():
    getDocumentsMetadataMock = MagicMock()
    getDocumentsStatusMock = MagicMock()
    documentFilterMock = MagicMock()
    
    with patch('application.service.get_documents_facade_service.LightDocument') as LightDocumentMock:
        getDocumentsFacadeService = GetDocumentsFacadeService(getDocumentsMetadataMock, getDocumentsStatusMock)
        
        getDocumentsMetadataMock.getDocumentsMetadata.return_value = []
        
        try:    
            response = getDocumentsFacadeService.getDocuments(documentFilterMock)
            assert False
        except ElaborationException:    
            getDocumentsMetadataMock.getDocumentsMetadata.assert_called_once_with(documentFilterMock)
            getDocumentsStatusMock.getDocumentsStatus.assert_not_called()
            LightDocumentMock.assert_not_called()
            pass
        
def test_getDocumentsFacadeServiceFailGetStatus():
    getDocumentsMetadataMock = MagicMock()
    getDocumentsStatusMock = MagicMock()
    documentFilterMock = MagicMock()
    documentMetadataMock = MagicMock()
    
    with patch('application.service.get_documents_facade_service.LightDocument') as LightDocumentMock:
        getDocumentsFacadeService = GetDocumentsFacadeService(getDocumentsMetadataMock, getDocumentsStatusMock)
        
        getDocumentsMetadataMock.getDocumentsMetadata.return_value = [documentMetadataMock]
        getDocumentsStatusMock.getDocumentsStatus.return_value = []
        
        try:    
            response = getDocumentsFacadeService.getDocuments(documentFilterMock)
            assert False
        except ElaborationException:    
            getDocumentsMetadataMock.getDocumentsMetadata.assert_called_once_with(documentFilterMock)
            getDocumentsStatusMock.getDocumentsStatus.assert_called_once_with([documentMetadataMock.id])
            LightDocumentMock.assert_not_called()
            pass
        
def test_getDocumentsFacadeServiceFailGetMetadataAndStatus():
    getDocumentsMetadataMock = MagicMock()
    getDocumentsStatusMock = MagicMock()
    documentFilterMock = MagicMock()
    
    with patch('application.service.get_documents_facade_service.LightDocument') as LightDocumentMock:
        getDocumentsFacadeService = GetDocumentsFacadeService(getDocumentsMetadataMock, getDocumentsStatusMock)
        
        getDocumentsMetadataMock.getDocumentsMetadata.return_value = []
        getDocumentsStatusMock.getDocumentsStatus.return_value = []
        
        try:    
            response = getDocumentsFacadeService.getDocuments(documentFilterMock)
            assert False
        except ElaborationException:    
            getDocumentsMetadataMock.getDocumentsMetadata.assert_called_once_with(documentFilterMock)
            getDocumentsStatusMock.getDocumentsStatus.assert_not_called()
            LightDocumentMock.assert_not_called()
            pass