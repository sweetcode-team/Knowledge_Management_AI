from typing import List

import chromadb

from adapter.out.persistence.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from langchain_core.documents.base import Document as LangchainCoreDocument

class VectorStoreChromaDBManager(VectorStoreManager):
    def __init__(self):
        cromadb = chromadb.PersistentClient(path="db")
        self.collection = cromadb.get_or_create_collection("knowledge_management_AI")

    #def getDocumentsStatus(documentsIds: List[str]): List[VectorStoreDocumentStatusResponse]
        #TODO
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponseList = []
        for documentId in documentsIds:
            try:
                self.collection.delete(where = {"source": documentId})
                vectorStoreDocumentOperationResponseList.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
            except:
                vectorStoreDocumentOperationResponseList.append(VectorStoreDocumentOperationResponse(documentId, False, "Eliminazione embeddings fallita."))
                continue
        return vectorStoreDocumentOperationResponseList

    
    def concealDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
     
    def uploadEmbeddings(self, documentsId: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId, documentChunks, documentEmbeddings in zip(documentsId, documentsChunks, documentsEmbeddings): 
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            metadatas = [{"text": chunk.page_content, "page": chunk.metadata.get('page'), "source": chunk.metadata.get('source')} for chunk in documentChunks]
            try:
                self.collection.add(
                        embeddings= documentEmbeddings,
                        metadatas= metadatas,
                        ids= ids
                    )
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Creazione embeddings avvenuta con succcesso."))
            except:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, "Creazione embeddings fallita."))
                continue
        return vectorStoreDocumentOperationResponses
            