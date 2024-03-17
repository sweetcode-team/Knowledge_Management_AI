from typing import List

from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from application.port.out.delete_documents_port import DeleteDocumentsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This class is the implementation of the DeleteDocumentsPort interface. It uses the AWSS3Manager to delete the documents.
    Attributes:
        awss3manager (AWSS3Manager): The AWSS3Manager to use to delete the documents.
"""
class DeleteDocumentsAWSS3(DeleteDocumentsPort):
    def __init__(self, awss3manager: AWSS3Manager):
        self.awss3manager = awss3manager
        
    """
    Deletes the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to delete.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because awss3manager needs a List of string
        documentsIdsString = [documentId.id for documentId in documentsIds]
        awsDocumentOperationResponseList = self.awss3manager.deleteDocuments(documentsIdsString)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for awsDocumentOperationResponse in awsDocumentOperationResponseList:
            documentOperationResponseList.append(awsDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList