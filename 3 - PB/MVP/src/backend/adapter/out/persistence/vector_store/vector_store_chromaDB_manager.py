import os
from typing import List
import chromadb
from langchain_core.retrievers import BaseRetriever

from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse
from langchain_core.documents.base import Document as LangchainCoreDocument
from langchain_community.vectorstores import Chroma
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel

"""
This class is the implementation of the VectorStoreManager interface. It uses the ChromaDB to manage the documents embeddings.
    Attributes:
        chromadb (chromadb.PersistentClient): The ChromaDB to use to manage the documents embeddings.
        collection (chromadb.Collection): The collection of the ChromaDB to use to manage the documents embeddings.
"""
class VectorStoreChromaDBManager(VectorStoreManager):
    def __init__(self):
        self.chromadb = chromadb.PersistentClient(path=os.environ.get("CHROMA_DB_PATH"))
        with open('/run/secrets/chromadb_collection', 'r') as file:
            chromadbCollection = file.read()
        self.collection = self.chromadb.get_or_create_collection(chromadbCollection)

    """
    Gets the status of the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to get the status.
    Returns:
        List[VectorStoreDocumentStatusResponse]: The response of the operation.
    """

    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        vectorStoreDocumentStatusResponses = []
        for documentId in documentsIds:
            try:
                chunksMetadata = self.collection.get(where={"source": documentId}, include = ["metadatas"]).get('metadatas', [])
                
                documentStatus = {chunkMetadata.get("status", "") for chunkMetadata in chunksMetadata}
                documentStatus.discard("")
                
                if len(documentStatus) == 0:
                    vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, 'NOT_EMBEDDED'))
                elif len(documentStatus) == 1:
                    vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, documentStatus.pop()))
                else:
                    vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, 'INCONSISTENT'))
            except:
                vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, None))
                continue
        
        return vectorStoreDocumentStatusResponses
    """
    Deletes the documents embeddings and returns the response.
    Args:
        documentsIds (List[str]): The documents to delete the embeddings.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                self.collection.delete(where = {"source": documentId})
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nell'eliminazione degli embeddings."))
                continue
        
        return vectorStoreDocumentOperationResponses
   
    """
    Conceals the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to conceal.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.  
    """
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        
        for documentId in documentsIds:
            try:
                embeddingsIds=(self.collection.get(where = {"source" : documentId})).get("ids", None)
                self.collection.update(
                    ids=embeddingsIds,
                    metadatas=[{"status": "CONCEALED"} for _ in range(len(embeddingsIds))])
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento occultato con successo."))
            except Exception as e:
                print(e, flush=True)
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nell'occultamento del documento."))
                continue
        
        return vectorStoreDocumentOperationResponses        
    """
    Disables the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to disable.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []

        for documentId in documentsIds:
            try:
                embeddingsIds=(self.collection.get(where = {"source" : documentId})).get("ids", None)
                self.collection.update(
                    ids=embeddingsIds,
                    metadatas=[{"status": "ENABLED"} for _ in range(len(embeddingsIds))])
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento riabilitato con successo."))
            except Exception as e:
                print(e, flush=True)
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nella riabilitazione del documento."))
                continue
            
        return vectorStoreDocumentOperationResponses   
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
        vectorStoreDocumentOperationResponses = []
        
        for documentId, documentChunks, documentEmbeddings in zip(documentsIds, documentsChunks, documentsEmbeddings): 
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            
            metadatas = [
                {
                    "page": chunk.metadata.get('page', 'NULL'),
                    "source": chunk.metadata.get('source', documentId),
                    "status": 'ENABLED'
                } for chunk in documentChunks
            ]

            try:
                self.collection.add(
                        ids = ids,
                        embeddings = documentEmbeddings,
                        documents = [chunk.page_content for chunk in documentChunks], 
                        metadatas = metadatas
                    )
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Creazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nel caricamento degli embeddings."))
                continue
        return vectorStoreDocumentOperationResponses

    """
    Changes the vector store and returns the response.
    Args:
        userId (int): The id of the user.
        vectorStore (str): The vector store to change.
    Returns:
        VectorStoreDocumentOperationResponse: The response of the operation.
    """
    def getRetriever(self, embeddingModel : LangchainEmbeddingModel) -> BaseRetriever:
        return Chroma(client=self.chromadb, collection_name = self.collection.name, embedding_function=embeddingModel.getEmbeddingFunction()).as_retriever(search_type="similarity_score_threshold", search_kwargs={'filter': {'status':'ENABLED'}, 'score_threshold': 0.5})