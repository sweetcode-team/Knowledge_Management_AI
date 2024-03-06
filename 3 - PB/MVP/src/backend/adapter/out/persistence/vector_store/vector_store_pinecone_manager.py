from typing import List
from pinecone import Pinecone
from pinecone import PineconeApiException
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse
from langchain_core.documents.base import Document as LangchainCoreDocument

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
        self.dimension = self.pinecone.describe_index(pineconeIndexName).get('dimension', 768)

    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]: #CONTROLLARE
        vectorStoreDocumentStatusResponses = []
        for documentId in documentsIds:
            try:
                queryResponse = self.index.query(
                    top_k = 1,
                    vector = [0.0 for _ in range(self.dimension)],
                    include_values = False,
                    include_metadata = True,
                    filter = {
                        "source": {"$eq": documentId}
                    }
                )
                vectorStoreDocumentStatusResponses.append(
                    VectorStoreDocumentStatusResponse(
                        documentId,
                        queryResponse.get('matches', [{}])[0].get('metadata', {}).get('status', 'NOT_EMBEDDED')
                    )
                )
            except PineconeApiException:
                vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, None))

        return vectorStoreDocumentStatusResponses

    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                queryResponse = self.index.query(
                                    top_k = 10000,
                                    vector = [0.0 for _ in range(self.dimension)],
                                    include_values = False,
                                    include_metadata = False,
                                    filter = {
                                        "source": {"$eq": documentId}
                                    }
                                )
                ids = [match.get('id', '') for match in queryResponse.get('matches', [{}])]
                if ids:
                    deleteResponse = self.index.delete(ids=ids)
                    if deleteResponse:
                        vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{deleteResponse.get('message', "Errore nell'eliminazione degli embeddings.")}"))
                    else:
                        vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
            except PineconeApiException as e:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nell'eliminazione degli embeddings: {e}"))

        return vectorStoreDocumentOperationResponses
    
  
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]: #CONTROLLARE
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                queryResponse = self.index.query(
                                    top_k = 10000,
                                    vector = [0.0 for _ in range(self.dimension)],
                                    include_values = False,
                                    include_metadata = False,
                                    filter = {
                                        "source": {"$eq": documentId}
                                    }
                                )
                documentEmbeddings = [match.get('id', '') for match in queryResponse.get('matches', [{}])] 
                concealResponse = self.index.update(
                        ids = documentEmbeddings,
                        set_metadata = {"status": "CONCEALED"}
                    )
                if concealResponse:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{concealResponse.get('message', "Errore nell'occultamento degli embeddings.")}"))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento occultato con successo."))
            except PineconeApiException as e:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nell'occultamento del documento: {e}"))
        
        return vectorStoreDocumentOperationResponses
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]: #CONTROLLARE
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            try:
                queryResponse = self.index.query(
                                    top_k = 10000,
                                    vector = [0.0 for _ in range(self.dimension)],
                                    include_values = False,
                                    include_metadata = False,
                                    filter = { 
                                        "source": {"$eq": documentId}
                                    }
                                )
                documentEmbeddings = [match.get('id', '') for match in queryResponse.get('matches', [{}])] 
                enableResponse = self.index.update(
                        ids = documentEmbeddings,
                        set_metadata = {"status": "ENABLED"}
                    )
                if enableResponse:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{enableResponse.get('message', "Errore nella riabilitazione del documento.")}"))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento riabilitato con successo."))
            except PineconeApiException as e:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nella riabilitazione del documento: {e}"))
        
        return vectorStoreDocumentOperationResponses
     
    def uploadEmbeddings(self, documentsId: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId, documentChunks, documentEmbeddings in zip(documentsId, documentsChunks, documentsEmbeddings):
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            metadatas = [{"text": chunk.page_content, "page": chunk.metadata.get('page'), "source": chunk.metadata.get('source'), "status": chunk.metadata.get('status')} for chunk in documentChunks]
            try:
                uploadResponse = self.index.upsert(
                        vectors = [
                            {
                                "id": id,
                                "values": documentEmbedding,
                                "metadata": metadata
                            } for id, metadata, documentEmbedding in zip(ids, metadatas, documentEmbeddings)
                        ]
                    )

                if uploadResponse.get('upserted_count', 0) != len(documentChunks):
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{uploadResponse.get('message', "Errore nel caricamento degli embeddings.")}"))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Creazione embeddings avvenuta con successo."))
            except PineconeApiException as e:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nel caricamento degli embeddings: {e}"))
            
        return vectorStoreDocumentOperationResponses
        