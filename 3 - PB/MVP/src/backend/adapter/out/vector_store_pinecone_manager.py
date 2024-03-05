from typing import List

import pinecone
from langchain.vectorstores import Pinecone

from adapter.out.persistence.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse

class VectorStorePineconeManager(VectorStoreManager):
    def __init__(self, pinecone_api, index_name, index_dimension, pinecone_environment):
        with open('/run/secrets/pinecone_api', 'r') as file:
            pineconeApi = file.read()
        with open('/run/secrets/pinecone_enviroment', 'r') as file:
            pineconeEnvironment = file.read()
            
        self.pinecone = pinecone.init(
            api_key=pineconeApi, 
            enviroment=pineconeEnvironment)
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def concealDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass

    def uploadEmbeddings(documentEmbeddings: List[tuple[str, List[float], dict[str, any]]]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    # def getDocumentsStatus(documentsIds: List[str]): List[VectorStoreDocumentStatusResponse]
    # TODO
