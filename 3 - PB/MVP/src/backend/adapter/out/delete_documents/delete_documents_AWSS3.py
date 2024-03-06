from typing import List

from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from application.port.out.delete_documents_port import DeleteDocumentsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

class DeleteDocumentsAWSS3(DeleteDocumentsPort):
    def __init__(self, awss3manager: AWSS3Manager):
        self.awss3manager = awss3manager
        
        
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because awss3manager needs a ListOfString
        documentsIdsString = [documentId.id for documentId in documentsIds]
        awsDocumentOperationResponseList = self.awss3manager.deleteDocuments(documentsIdsString)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for awsDocumentOperationResponse in awsDocumentOperationResponseList:
            documentOperationResponseList.append(awsDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList