from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain

def test_uploadEmbeddingsTrue():
    with    patch('adapter.out.upload_documents.embeddings_uploader_facade_langchain.DocumentOperationResponse') as DocumentOperationResponseMock, \
            patch('adapter.out.upload_documents.embeddings_uploader_facade_langchain.DocumentId') as DocumentIdMock, \
            patch('adapter.out.upload_documents.embeddings_uploader_facade_langchain.LangchainDocument') as LangchainDocumentMock:
        chunkerizerMock = MagicMock()
        embeddingsCreatorMock = MagicMock()
        embeddingsUploaderVectorStoreMock = MagicMock()
        documentMock = MagicMock()
        langchainDocumentMock = MagicMock()
        vectorStoreDocumentOperationResponseMock = MagicMock()
        
        chunkerizerMock.extractText.return_value = [langchainDocumentMock]
        embeddingsCreatorMock.embedDocument.return_value = [[1.0, 2.0, 3.0]]
        embeddingsUploaderVectorStoreMock.uploadEmbeddings.return_value = [vectorStoreDocumentOperationResponseMock]
        vectorStoreDocumentOperationResponseMock.documentId = "Prova.pdf"
        vectorStoreDocumentOperationResponseMock.ok.return_value = True
        vectorStoreDocumentOperationResponseMock.message = "OK"
        documentMock.plainDocument.metadata.id.id = "Prova.pdf"
        
        
        embeddingsUploaderFacadeLangchain = EmbeddingsUploaderFacadeLangchain(chunkerizerMock, embeddingsCreatorMock, embeddingsUploaderVectorStoreMock)
        
        response = embeddingsUploaderFacadeLangchain.uploadEmbeddings([documentMock])
        
        LangchainDocumentMock.assert_called_once_with(documentId='Prova.pdf', 
                                                      chunks=[langchainDocumentMock], 
                                                      embeddings=[[1.0, 2.0, 3.0]])
        DocumentIdMock.assert_called_once_with('Prova.pdf')
        DocumentOperationResponseMock.assert_called_once_with(DocumentIdMock(), True, "OK")
        
        assert response == [DocumentOperationResponseMock()]
        
def test_uploadEmbeddingsFail():
    with    patch('adapter.out.upload_documents.embeddings_uploader_facade_langchain.DocumentOperationResponse') as DocumentOperationResponseMock, \
            patch('adapter.out.upload_documents.embeddings_uploader_facade_langchain.DocumentId') as DocumentIdMock, \
            patch('adapter.out.upload_documents.embeddings_uploader_facade_langchain.LangchainDocument') as LangchainDocumentMock:
        chunkerizerMock = MagicMock()
        embeddingsCreatorMock = MagicMock()
        embeddingsUploaderVectorStoreMock = MagicMock()
        documentMock = MagicMock()
        langchainDocumentMock = MagicMock()
        vectorStoreDocumentOperationResponseMock = MagicMock()
        
        chunkerizerMock.extractText.return_value = [langchainDocumentMock]
        embeddingsCreatorMock.embedDocument.return_value = [[1.0, 2.0, 3.0]]
        embeddingsUploaderVectorStoreMock.uploadEmbeddings.return_value = [vectorStoreDocumentOperationResponseMock]
        vectorStoreDocumentOperationResponseMock.documentId = "Prova.pdf"
        vectorStoreDocumentOperationResponseMock.ok.return_value = False
        vectorStoreDocumentOperationResponseMock.message = "KO"
        documentMock.plainDocument.metadata.id.id = "Prova.pdf"
        
        
        embeddingsUploaderFacadeLangchain = EmbeddingsUploaderFacadeLangchain(chunkerizerMock, embeddingsCreatorMock, embeddingsUploaderVectorStoreMock)
        
        response = embeddingsUploaderFacadeLangchain.uploadEmbeddings([documentMock])
        
        LangchainDocumentMock.assert_called_once_with(documentId='Prova.pdf', 
                                                      chunks=[langchainDocumentMock], 
                                                      embeddings=[[1.0, 2.0, 3.0]])
        DocumentIdMock.assert_called_once_with('Prova.pdf')
        DocumentOperationResponseMock.assert_called_once_with(DocumentIdMock(), False, "KO")
        
        assert response == [DocumentOperationResponseMock()]