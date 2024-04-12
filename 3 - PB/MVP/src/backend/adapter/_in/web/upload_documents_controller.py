from typing import List

from adapter._in.web.presentation_domain.new_document import NewDocument
from application.port._in.upload_documents_use_case import UploadDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse

from domain.exception.exception import ElaborationException
from api_exceptions import APIElaborationException

"""
This class is the controller for the upload documents use case. It receives the new documents and converts them to the domain model.
It also receives the force upload parameter and sends the documents to the use case.
    Attributes:
        useCase (UploadDocumentsUseCase): The use case for uploading documents.
"""
class UploadDocumentsController:
    def __init__(self, uploadDocumentsUseCase: UploadDocumentsUseCase):
        self.useCase = uploadDocumentsUseCase

    def uploadDocuments(self, newDocuments: List[NewDocument], forceUpload: bool = False) -> List[DocumentOperationResponse]:
        """
        Receives the new documents and the force upload parameter and sends them to the use case.
        Args:
            newDocuments (List[NewDocument]): The new documents.
            forceUpload (bool): The force upload parameter.
        Returns:
            List[DocumentOperationResponse]: the response of the operation.
        """
        try:
            documents = [newDocument.toDocument() for newDocument in newDocuments]
            return self.useCase.uploadDocuments(documents, forceUpload)
        except ElaborationException as e:
            raise APIElaborationException(str(e))
    
