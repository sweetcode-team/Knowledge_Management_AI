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

    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        vectorStoreDocumentStatusResponses = []
        for documentId in documentsIds:
            try:
                vector = self.collection.get(where={"source": documentId})
                print(vector, flush=True)
                vectorStoreDocumentStatusResponses.append(VectorStoreDocumentOperationResponse(documentId, status=vector.get("status", "provaTrue")))
            except:
                vectorStoreDocumentStatusResponses.append(
                    VectorStoreDocumentStatusResponse(documentId, status="provaFalse"))
                continue
        return vectorStoreDocumentStatusResponses
    
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
   
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                embeddingsIds=(self.collection.get(where = {"source" : documentId})).get("ids", None)
                self.collection.update(
                    ids=embeddingsIds,
                    metadatas={"status": "CONCEALED"})
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento occultato con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nell'occultamento del documento."))
                continue 
        return vectorStoreDocumentOperationResponses        
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []

        for documentId in documentsIds:
            try:
                embeddingsIds=(self.collection.get(where = {"source" : documentId})).get("ids", None)
                self.collection.update(
                    ids=embeddingsIds,
                    metadatas={"status": "ENABLED"})
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento riabilitato con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nella riabilitazione del documento."))
                continue
        return vectorStoreDocumentOperationResponses   
     
    def uploadEmbeddings(self, documentsIds: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId, documentChunks, documentEmbeddings in zip(documentsIds, documentsChunks, documentsEmbeddings): 
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            metadatas = [{"page": chunk.metadata.get('page', 'NULL'), "source": chunk.metadata.get('source'), "status": chunk.metadata.get('status')} for chunk in documentChunks]

            try:
                self.collection.add(
                        embeddings = documentEmbeddings,
                        documents = [chunk.page_content for chunk in documentChunks], 
                        metadatas = metadatas,
                        ids = ids
                    )
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Creazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nel caricamento degli embeddings."))
                continue
        return vectorStoreDocumentOperationResponses
            