from datetime import datetime
"""
This class is used to store the metadata of a document stored in AWS S3.
"""
class AWSDocumentMetadata:
    def __init__(self, id: str, size: float, uploadTime: datetime):
        self.id = id
        self.size = size
        self.uploadTime = uploadTime
