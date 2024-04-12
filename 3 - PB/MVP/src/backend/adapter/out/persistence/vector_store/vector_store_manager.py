from typing import List

from langchain_core.retrievers import BaseRetriever

from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse

from langchain_core.documents.base import Document as LangchainCoreDocument

from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel

"""
This interface is used to manage the documents embeddings.
"""
class VectorStoreManager:
    """
    Gets the status of the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to get the status.
    Returns:
        List[VectorStoreDocumentStatusResponse]: The response of the operation.
    """
    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        pass
    
    """
    Deletes the documents embeddings and returns the response.
    Args:
        documentsIds (List[str]): The documents to delete the embeddings.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    """
    Conceals the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to conceal.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
   
    """
    Enables the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to enable.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """ 
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
       
    """
    Uploads the documents embeddings and returns the response.
    Args:
        documentsIds (List[str]): The documents to upload the embeddings.
        documentsChunks (List[List[LangchainCoreDocument]]): The documents chunks to upload the embeddings.
        documentsEmbeddings (List[List[List[float]]]): The documents embeddings to upload.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """ 
    def uploadEmbeddings(self, documentsIds: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        pass
       
    """
    Gets the retriever.
    Args:
        embeddingModel (LangchainEmbeddingModel): The embedding model to use.
    Returns:
        BaseRetriever: The retriever.
    """ 
    def getRetriever(self, embeddingModel : LangchainEmbeddingModel) -> BaseRetriever:
        pass