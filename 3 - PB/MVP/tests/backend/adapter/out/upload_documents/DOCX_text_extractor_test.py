from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.DOCX_text_extractor import DOCXTextExtractor

def test_extractText():
    with    patch('adapter.out.upload_documents.DOCX_text_extractor.tempfile.NamedTemporaryFile') as tempfileMock, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.Docx2txtLoader') as docx2txtLoaderMock, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.RecursiveCharacterTextSplitter') as recursiveCharacterTextSplitterMock:
            documentContentMock = MagicMock()
            documentLangchainMock = MagicMock()
            
            documentContentMock.content = "content"
            tempfileMock.write.return_value = None
            tempfileMock.name = "tempFile"
            docx2txtLoaderMock.return_value = docx2txtLoaderMock
            docx2txtLoaderMock.load.return_value = [documentLangchainMock]
            recursiveCharacterTextSplitterMock.return_value = recursiveCharacterTextSplitterMock
            recursiveCharacterTextSplitterMock.split_documents.return_value = [documentLangchainMock]
            
            docxTextExtractor = DOCXTextExtractor()
            
            response = docxTextExtractor.extractText(documentContentMock)
            
            assert isinstance(response, list)
            assert response == [documentLangchainMock]