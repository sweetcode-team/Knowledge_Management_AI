from typing import List
import chromadb
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse
from langchain_core.documents.base import Document as LangchainCoreDocument

class VectorStoreChromaDBManager(VectorStoreManager):
    def __init__(self):
        cromadb = chromadb.PersistentClient(path="db")
        self.collection = cromadb.get_or_create_collection("kmai-collection")

    def getDocumentsStatus(documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        pass
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                self.collection.delete(where = {"source": documentId})
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Eliminazione embeddings fallita."))
                continue
        return vectorStoreDocumentOperationResponses
   
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                embeddingsIds=(self.collection.get(where = {"source" : documentId})).get("ids", None)
                self.collection.update(
                    ids=embeddingsIds,
                    metadatas={"status": "CONCEALED"})
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Occultazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Occultazione embeddings fallita."))
                continue         
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                embeddingsIds=(self.collection.get(where = {"source" : documentId})).get("ids", None)
                self.collection.update(
                    ids=embeddingsIds,
                    metadatas={"status": "ENABLED"})
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Riabilitazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Riabilitazione embeddings fallita."))
                continue
        return vectorStoreDocumentOperationResponses   
     
    def uploadEmbeddings(self, documentsIds: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId, documentChunks, documentEmbeddings in zip(documentsIds, documentsChunks, documentsEmbeddings): 
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            metadatas = [{"page": chunk.metadata.get('page'), "source": chunk.metadata.get('source'), "status": chunk.metadata.get('status')} for chunk in documentChunks]
            try:
                self.collection.add(
                        embeddings = documentEmbeddings,
                        documents = [chunk.page_content for chunk in documentChunks], 
                        metadatas = metadatas,
                        ids = ids
                    )
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Creazione embeddings avvenuta con succcesso."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Creazione embeddings fallita."))
                continue
        return vectorStoreDocumentOperationResponses
            