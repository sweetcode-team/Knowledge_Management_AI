import os
from typing import List
import chromadb
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse
from langchain_core.documents.base import Document as LangchainCoreDocument

class VectorStoreChromaDBManager(VectorStoreManager):
    def __init__(self):
        cromadb = chromadb.PersistentClient(path=os.environ.get("CHROMA_DB_PATH"))
        with open('/run/secrets/chromadb_collection', 'r') as file:
            chromadbCollection = file.read()
        self.collection = cromadb.get_or_create_collection(chromadbCollection)

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
                    metadatas=[{"status": "CONCEALED"} for _ in range(len(embeddingsIds))])
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento occultato con successo."))
            except Exception as e:
                print(e, flush=True)
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
                    metadatas=[{"status": "ENABLED"} for _ in range(len(embeddingsIds))])
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento riabilitato con successo."))
            except Exception as e:
                print(e, flush=True)
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Errore nella riabilitazione del documento."))
                continue
            
        return vectorStoreDocumentOperationResponses   
     
    def uploadEmbeddings(self, documentsIds: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        
        for documentId, documentChunks, documentEmbeddings in zip(documentsIds, documentsChunks, documentsEmbeddings): 
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            
            metadatas = [
                {
                    "page": chunk.metadata.get('page', 'NULL'),
                    "source": chunk.metadata.get('source', documentId),
                    "status": chunk.metadata.get('status', 'ENABLED')
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
            