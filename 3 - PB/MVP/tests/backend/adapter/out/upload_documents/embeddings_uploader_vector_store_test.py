from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore

def test_uploadEmbeddings():
    vectorStoreManagerMock = MagicMock()
    langchainDocumentMock = MagicMock()
    documentChunkMock = MagicMock()
    
    langchainDocumentMock.documentId = "Prova.pdf"
    langchainDocumentMock.chunks = [documentChunkMock]
    langchainDocumentMock.embeddings = [[1.0, 2.0, 3.0]]
    
    response = EmbeddingsUploaderVectorStore(vectorStoreManagerMock).uploadEmbeddings([langchainDocumentMock])
    
    vectorStoreManagerMock.uploadEmbeddings.assert_called_once_with(("Prova.pdf",), ([documentChunkMock],), ([[1.0, 2.0, 3.0]],))
    assert response == vectorStoreManagerMock.uploadEmbeddings.return_value