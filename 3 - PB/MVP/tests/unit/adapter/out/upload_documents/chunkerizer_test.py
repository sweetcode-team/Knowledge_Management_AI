from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.chunkerizer import Chunkerizer
        
def test_extractTextPDF():
    with patch('adapter.out.upload_documents.chunkerizer.PDFTextExtractor') as PDFTextExtractorMock:
        documentMock = MagicMock()
        documentChunkMock = MagicMock()
        statusMock = MagicMock()

        statusMock.ENABLED.name = "ENABLED"
        documentMock.plainDocument.metadata.type.name = "PDF"
        documentMock.plainDocument.metadata.id.id = "Prova.pdf"
        documentMock.documentStatus.status = statusMock.ENABLED

        PDFTextExtractorMock.return_value = PDFTextExtractorMock
        PDFTextExtractorMock.return_value.extractText.return_value = [documentChunkMock]
        
        documentChunkMock.metadata = {}
        
        chunkerizer = Chunkerizer()
        response = chunkerizer.extractText(documentMock)
        
        assert isinstance(response, list)
        assert response[0] == documentChunkMock
        assert response[0].metadata["source"] == "Prova.pdf"
        assert response[0].metadata["status"] == "ENABLED"
        
def test_extractTextDOCX():
    with patch('adapter.out.upload_documents.chunkerizer.DOCXTextExtractor') as DOCXTextExtractorMock:
        documentMock = MagicMock()
        documentChunkMock = MagicMock()
        statusMock = MagicMock()

        statusMock.ENABLED.name = "ENABLED"
        documentMock.plainDocument.metadata.type.name = "DOCX"
        documentMock.plainDocument.metadata.id.id = "Prova.docx"
        documentMock.documentStatus.status = statusMock.ENABLED

        DOCXTextExtractorMock.return_value = DOCXTextExtractorMock
        DOCXTextExtractorMock.return_value.extractText.return_value = [documentChunkMock]
        
        documentChunkMock.metadata = {}
        
        chunkerizer = Chunkerizer()
        response = chunkerizer.extractText(documentMock)
        
        assert isinstance(response, list)
        assert response[0] == documentChunkMock
        assert response[0].metadata["source"] == "Prova.docx"
        assert response[0].metadata["status"] == "ENABLED"
        
def test_extractTextFail():
    documentMock = MagicMock()
    
    documentMock.plainDocument.metadata.type.name = "ErrorTestType"
    
    chunkerizer = Chunkerizer()
    
    response = chunkerizer.extractText(documentMock)
    
    assert response == []
        
def test_getTextExtractorFromPDF():
    with patch('adapter.out.upload_documents.chunkerizer.PDFTextExtractor') as PDFTextExtractorMock:  
        
        PDFTextExtractorMock.return_value = PDFTextExtractorMock
          
        chunkerizer = Chunkerizer()
        
        response = chunkerizer.getTextExtractorFrom("PDF")
   
        assert response == PDFTextExtractorMock
        
def test_getTextExtractorFromDOCX():
    with patch('adapter.out.upload_documents.chunkerizer.DOCXTextExtractor') as DOCXTextExtractorMock:  
        
        DOCXTextExtractorMock.return_value = DOCXTextExtractorMock
          
        chunkerizer = Chunkerizer()
        
        response = chunkerizer.getTextExtractorFrom("DOCX")
   
        assert response == DOCXTextExtractorMock
        
def test_getTextExtractorFromFail():
    chunkerizer = Chunkerizer()
    
    response = chunkerizer.getTextExtractorFrom("ErrorTestType")
    
    assert response == None