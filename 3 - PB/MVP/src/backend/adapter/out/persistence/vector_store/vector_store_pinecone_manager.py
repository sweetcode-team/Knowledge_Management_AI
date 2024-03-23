from typing import List

from langchain_core.retrievers import BaseRetriever
from pinecone import Pinecone
from pinecone import PineconeApiException
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse
from langchain_core.documents.base import Document as LangchainCoreDocument
from langchain_community.vectorstores import Pinecone as PineconeLangchain
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel

   
""" 
    This class is the implementation of the VectorStoreManager interface. It uses the Pinecone to manage the documents embeddings.
        Attributes:
            pinecone (Pinecone): The Pinecone to use to manage the documents embeddings.
            index (Pinecone.Index): The index of the Pinecone to use to manage the documents embeddings.
            dimension (int): The dimension of the embeddings.
""" 
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
            environment=pineconeEnvironment
        )
        self.index = self.pinecone.Index(pineconeIndexName)
        self.dimension = self.pinecone.describe_index(pineconeIndexName).get('dimension', 768)

   
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
                queryResponse = self.index.query(
                    top_k = 1,
                    vector = [0.0 for _ in range(self.dimension)],
                    include_values = False,
                    include_metadata = True,
                    filter = {
                        "source": {"$eq": documentId}
                    }
                )
                documentStatus = {documentEmbeddingsMatch.get('metadata', {}).get('status', None) for documentEmbeddingsMatch in queryResponse.get('matches', [])}
                documentStatus.discard(None)
                
                if len(documentStatus) == 0:
                    vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, 'NOT_EMBEDDED'))
                elif len(documentStatus) == 1:
                    vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, documentStatus.pop()))
                else:
                    vectorStoreDocumentStatusResponses.append(VectorStoreDocumentStatusResponse(documentId, 'INCONSISTENT'))
            except PineconeApiException:
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
                queryResponse = self.index.query(
                                    top_k = 10000,
                                    vector = [0.0 for _ in range(self.dimension)],
                                    include_values = False,
                                    include_metadata = False,
                                    filter = {
                                        "source": {"$eq": documentId}
                                    }
                                )
                ids = {match.get('id', '') for match in queryResponse.get('matches', [])}
                ids.discard('')
                
                if len(ids) > 0:
                    deleteResponse = self.index.delete(ids=list(ids))
                    if deleteResponse:
                        vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{deleteResponse.get('message', 'Errore nella eliminazione degli embeddings.')}"))
                    else:
                        vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Nessun embedding trovato da eliminare."))
            except PineconeApiException as e:
                vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nell'eliminazione degli embeddings: {e}"))

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
            messageError = []
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
                flagError = False
                for documentEmbedding in documentEmbeddings:
                    concealResponse = self.index.update(
                            id = documentEmbedding,
                            set_metadata = {"status": "CONCEALED"}
                        )
                    if concealResponse:
                        flagError = True
                        messageError.append(concealResponse.get('message', "Errore nell'occultamento del documento."))
                if flagError:
                    concatenated_messages = "-".join(messageError)
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{concatenated_messages}"))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento occultato con successo."))
            except PineconeApiException as e:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nell'occultamento del documento: {e}"))
        
        return vectorStoreDocumentOperationResponses
    
       
    """
    Enables the documents and returns the response.
    Args:
        documentsIds (List[str]): The documents to enable.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """ 
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]: 
        vectorStoreDocumentOperationResponses = []
        for documentId in documentsIds:
            messageError = []
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
                flagError = False
                for documentEmbedding in documentEmbeddings:
                    concealResponse = self.index.update(
                            id = documentEmbedding,
                            set_metadata = {"status": "ENABLED"}
                        )
                    if concealResponse:
                        flagError = True
                        messageError.append(concealResponse.get('message', "Errore nella riabilitazione del documento."))
                if flagError:
                    concatenated_messages = "-".join(messageError)
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{concatenated_messages}"))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Documento riabilitato con successo."))
            except PineconeApiException as e:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nella riabilitazione del documento: {e}"))
        
        return vectorStoreDocumentOperationResponses
     
        
    """ 
    Uploads the documents embeddings and returns the response.
    Args:
        documentsId (List[str]): The documents to upload the embeddings.
        documentsChunks (List[List[LangchainCoreDocument]]): The documents chunks to upload the embeddings.
        documentsEmbeddings (List[List[List[float]]]): The documents embeddings to upload.
    Returns:
        List[VectorStoreDocumentOperationResponse]: The response of the operation.
    """ 
    def uploadEmbeddings(self, documentsId: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponses = []
        for documentId, documentChunks, documentEmbeddings in zip(documentsId, documentsChunks, documentsEmbeddings):
            ids=[f"{documentId}@{i}" for i in range(len(documentChunks))]
            
            metadatas = [
                {
                    "text": documentChunk.page_content,
                    "page": documentChunk.metadata.get('page',-1),
                    "source": documentChunk.metadata.get('source', documentId),
                    "status": documentChunk.metadata.get('status', 'ENABLED')
                } for documentChunk in documentChunks
            ]

            try:
                uploadResponse = self.index.upsert(
                        vectors = [
                            {
                                "id": id,
                                "metadata": metadata,
                                "values": documentEmbedding
                            } for id, metadata, documentEmbedding in zip(ids, metadatas, documentEmbeddings)
                        ]
                    )

                if uploadResponse.get('upserted_count', 0) != len(documentChunks):
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"{uploadResponse.get('message', 'Errore nel caricamento degli embeddings.')}"))
                else:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, True, "Creazione embeddings avvenuta con successo."))
            except PineconeApiException as e:
                    vectorStoreDocumentOperationResponses.append(VectorStoreDocumentOperationResponse(documentId, False, f"Errore nel caricamento degli embeddings: {e}"))
            
        return vectorStoreDocumentOperationResponses

   
    """
    Gets the retriever.
    Args:
    LangchainEmbeddingModel: The embedding model to use to get the retriever.
    Returns:
    BaseRetriever: The retriever.

    """ 
    def getRetriever(self, embeddingModel : LangchainEmbeddingModel) -> BaseRetriever:
        return PineconeLangchain(self.index, embeddingModel.getEmbeddingFunction(), "text").as_retriever(search_type="similarity_score_threshold", search_kwargs={'filter': {'status':'ENABLED'}, 'score_threshold': 0.3})