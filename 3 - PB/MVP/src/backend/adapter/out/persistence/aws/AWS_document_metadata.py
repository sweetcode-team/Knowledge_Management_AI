from dataclasses import dataclass
from datetime import datetime

"""
This class is used to store the metadata of a document stored in AWS S3.
"""
@dataclass
class AWSDocumentMetadata:
    id: str
    size: float
    uploadTime: datetime
        
