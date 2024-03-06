from datetime import datetime
from dataclasses import dataclass
"""
    This class is used to represent a document that is stored in the AWS S3 bucket.
"""
@dataclass
class AWSDocument:
    id: str
    content: bytes
    type: str
    size: float
    uploadTime: datetime


