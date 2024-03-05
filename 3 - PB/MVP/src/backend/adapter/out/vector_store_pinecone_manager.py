from typing import List

from pinecone import Pinecone

from adapter.out.persistence.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse

class VectorStorePineconeManager(VectorStoreManager):
    def __init__(self):        
        with open('/run/secrets/pinecone_api', 'r') as file:
            pineconeApi = file.read()
        with open('/run/secrets/pinecone_enviroment', 'r') as file:
            pineconeEnvironment = file.read()
        with open('/run/secrets/pinecone_index_name', 'r') as file:
            pineconeIndexName = file.read()
            
        self.pinecone = pinecone.init(
            api_key=pineconeApi, 
            enviroment=pineconeEnvironment)
        self.index = self.pinecone.Index(pineconeIndexName)
        
    #def getDocumentsStatus(documentsIds: List[str]): List[VectorStoreDocumentStatusResponse]
        #TODO
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        vectorStoreDocumentOperationResponseList = []
        for documentId in documentsIds:
            deleteResponse = self.index.delete(ids=self.index.list(prefix=documentId))
            if deleteResponse:
                deleteResponse. 
            else:
                vectorStoreDocumentOperationResponseList.append(VectorStoreDocumentOperationResponse(documentId, True, "Eliminazione embeddings avvenuta con successo."))
        return vectorStoreDocumentOperationResponseList  
        
    
    def concealDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
     
    # def uploadEmbeddings(documentEmbeddings:)
        #TODO