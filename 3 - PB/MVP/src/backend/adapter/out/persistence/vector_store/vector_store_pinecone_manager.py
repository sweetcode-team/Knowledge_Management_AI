from typing import List

from pinecone import Pinecone

from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse

class VectorStorePineconeManager(VectorStoreManager):
    def __init__(self):
        with open('/run/secrets/pinecone_api', 'r') as file:
            pineconeApi = file.read()
        with open('/run/secrets/pinecone_environment', 'r') as file:
            pineconeEnvironment = file.read()
        with open('/run/secrets/pinecone_index_name', 'r') as file:
            pineconeIndexName = file.read()

        self.pinecone = Pinecone(
            api_key=pineconeApi, 
            environment=pineconeEnvironment)
        self.index = self.pinecone.Index(pineconeIndexName)

    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        vectorStoreDocumentStatusResponses = []
        for documentId in documentsIds:
            query_response = self.index.query(
                top_k=1,
                include_values=False,
                include_metadata=True,
                filter={
                    "name": {"$eq": documentId}
                }
            )
            vectorStoreDocumentStatusResponses.append(
                VectorStoreDocumentStatusResponse(
                    documentId,
                    query_response.get('matches', [{}])[0].get('metadata', {}).get('status', 'NOT_EMBEDDED')
                )
            )
        return vectorStoreDocumentStatusResponses

    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            deleteResponse = self.index.delete(
                    filter={
                        "name": {"$eq": documentId}
                    }
                )
            if deleteResponse:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{deleteResponse.get('message')}"))
            else:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
        
        return vectorStoreDocumentOperationResponses

    
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            documentEmbeddings = self.index.list(prefix=documentId)
            concealResponse = self.index.update(
                    ids=documentEmbeddings,
                    set_metadata={"status": "CONCEALED"}
                )
            if concealResponse:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{concealResponse.get('message')}"))
            else:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento occultato con successo."))
        
        return vectorStoreDocumentOperationResponses
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            documentEmbeddings = self.index.list(prefix=documentId)
            enableResponse = self.index.update(
                    ids=documentEmbeddings,
                    set_metadata={"status": "ENABLED"}
                )
            if enableResponse:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{enableResponse.get('message')}"))
            else:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento riabilitato con successo."))
        
        return vectorStoreDocumentOperationResponses
     
    # def uploadEmbeddings(self, documentsEmbeddings:)
        #TODO