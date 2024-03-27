from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.PDF_text_extractor import PDFTextExtractor

def test_extractText():
    with    patch('adapter.out.upload_documents.PDF_text_extractor.tempfile.NamedTemporaryFile') as tempfileMock, \
            patch('adapter.out.upload_documents.PDF_text_extractor.PyPDFLoader') as pyPDFLoaderMock, \
            patch('adapter.out.upload_documents.PDF_text_extractor.CharacterTextSplitter') as CharacterTextSplitterMock:
            documentContentMock = MagicMock()
            documentLangchainMock = MagicMock()
            
            documentContentMock.content = "content"
            tempfileMock.write.return_value = None
            tempfileMock.name = "tempFile"
            pyPDFLoaderMock.return_value = pyPDFLoaderMock
            pyPDFLoaderMock.load.return_value = [documentLangchainMock]
            CharacterTextSplitterMock.return_value = CharacterTextSplitterMock
            CharacterTextSplitterMock.split_documents.return_value = [documentLangchainMock]
            
            pdfTextExtractor = PDFTextExtractor()
            
            response = pdfTextExtractor.extractText(documentContentMock)
            
            assert isinstance(response, list)
            assert response == [documentLangchainMock]