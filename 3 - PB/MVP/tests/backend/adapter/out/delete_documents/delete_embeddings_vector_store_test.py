from unittest.mock import MagicMock, patch
from adapter.out.delete_documents.delete_embeddings_vector_store import DeleteEmbeddingsVectorStore
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_deleteDocumentsEmbeddingsTrue():
    embeddingsVectorStore = MagicMock()
    embeddingsVectorStoreDocumentOperationResponse = MagicMock()
    
    embeddingsVectorStoreDocumentOperationResponse.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted")
    embeddingsVectorStore.deleteDocumentsEmbeddings.return_value = [embeddingsVectorStoreDocumentOperationResponse]
    deleteEmbeddingsVectorStore = DeleteEmbeddingsVectorStore(embeddingsVectorStore)
    
    response = deleteEmbeddingsVectorStore.deleteDocumentsEmbeddings([DocumentId("Prova.pdf")])
   
    embeddingsVectorStore.deleteDocumentsEmbeddings.assert_called_once_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)
    
def test_deleteDocumentsEmbeddingsFail():
    embeddingsVectorStore = MagicMock()
    embeddingsVectorStoreDocumentOperationResponse = MagicMock()
    
    embeddingsVectorStoreDocumentOperationResponse.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Document not found")
    embeddingsVectorStore.deleteDocumentsEmbeddings.return_value = [embeddingsVectorStoreDocumentOperationResponse]
    deleteEmbeddingsVectorStore = DeleteEmbeddingsVectorStore(embeddingsVectorStore)
    
    response = deleteEmbeddingsVectorStore.deleteDocumentsEmbeddings([DocumentId("Prova.pdf")])
   
    embeddingsVectorStore.deleteDocumentsEmbeddings.assert_called_once_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)