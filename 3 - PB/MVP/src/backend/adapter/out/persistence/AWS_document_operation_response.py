"""
This class is used to store the metadata of a document stored in AWS S3.
"""
class AWSDocumentOperationResponse:
    def __init__(self, documentId: str, status: bool, message: str):
        self.documentId = documentId
        self.status = status
        self.message = message
