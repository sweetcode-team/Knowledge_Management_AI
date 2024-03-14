from typing import List
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.langchain_document import LangchainDocument

"""
This class is the implementation of the EmbeddingsUploaderPort interface. It uses the VectorStoreManager to upload the documents embeddings.
    Attributes:
        vectorStoreManager (VectorStoreManager): The VectorStoreManager to use to upload the documents embeddings.
"""
class EmbeddingsUploaderVectorStore:
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

   
    """
    Uploads the documents embeddings and returns the response.
    Args:
        documents (List[LangchainDocument]): The documents to upload the embeddings.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.   
    """ 
    def uploadEmbeddings(self, documents: List[LangchainDocument]) -> List[VectorStoreDocumentOperationResponse]:
        documentsId, documentsChunks, documentsEmbeddings = zip(*[(document.documentId, document.chunks, document.embeddings) for document in documents])
        return self.vectorStoreManager.uploadEmbeddings(documentsId, documentsChunks, documentsEmbeddings)
    