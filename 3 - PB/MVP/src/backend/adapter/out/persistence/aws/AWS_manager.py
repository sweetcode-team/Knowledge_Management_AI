import os
from typing import List

import boto3
from adapter.out.persistence.aws.AWS_document import AWSDocument
from adapter.out.persistence.aws.AWS_document_operation_response import AWSDocumentOperationResponse
from adapter.out.persistence.aws.AWS_document_metadata import AWSDocumentMetadata
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType

"""
    This class is responsible for managing the AWS S3 bucket.
    Attributes:
        s3 (boto3.client): The boto3 client for S3 operations.
        bucket_name (str): The name of the S3 bucket.
    Methods:
        getDocumentById(documentId: str) -> AWSDocument:
            Get the document from the S3 bucket by its ID.
        uploadDocuments(awsDocuments: List[AWSDocument], forceUpload: bool) -> List[AWSDocumentOperationResponse]:
            Upload the documents to the S3 bucket.
        deleteDocuments(ListOfDocumentId: List[str]) -> List[AWSDocumentOperationResponse]:
            Delete the documents from the S3 bucket.
        getDocumentsMetadata(documentFilter: str) -> List[AWSDocumentMetadata]:
            Get the metadata of the documents from the S3 bucket.
"""
class AWSS3Manager:
    def __init__(self):
        with open('/run/secrets/aws_access_key_id', 'r') as file:
            aws_access_key_id = file.read()
        with open('/run/secrets/aws_secret_access_key', 'r') as file:
            aws_secret_access_key = file.read()
        with open('/run/secrets/aws_bucket_name', 'r') as file:
            awsBucketName = file.read()
        self.awsBucketName = awsBucketName
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name="eu-west-1"
        )
    def getDocumentById(self, documentId):
        try:
            aws = self.s3.get_object(Bucket=self.awsBucketName, Key=documentId)
            id = aws.get('Key')
            content = aws.get('Body').read()
            type = aws.get('ContentType')
            size = aws.get('ContentLength')
            uploadTime = aws.get('LastModified')
        except:
            return None
        return AWSDocument(
            id,
            content,
            type,
            size,
            uploadTime
        )

    def uploadDocuments(self, awsDocuments: List[AWSDocument], forceUpload:bool) -> List[AWSDocumentOperationResponse]:
        AWSDocumentOperationResponseList = []
        status = True
        for document in awsDocuments:
            # if not forceUpload:
            #     try:
            #         self.s3.head_object(Bucket=self.awsBucketName, Key=document.id)
            #         message = "Document already exists"
            #         AWSDocumentOperationResponseList.append(AWSDocumentOperationResponse(document.id, status, message))
            #         continue
            #     except:
            #         pass
            # aws = self.s3.put_object(Bucket=self.awsBucketName, Key=document.id, Body=document.content, ContentType=document.type) # TODO
            #TODO status da cambiare, se funziona true, altrimenti false
            message = "Document uploaded successfully"
            AWSDocumentOperationResponseList.append(AWSDocumentOperationResponse(document.id, status, message))
        return AWSDocumentOperationResponseList

    def deleteDocuments(self, documentsIds: List[str]) -> List[AWSDocumentOperationResponse]:
        AWSDocumentOperationResponseList = []
        for documentId in documentsIds:
            status = True
            try:
                # self.s3.delete_object(Bucket=self.awsBucketName, Key=documentId) TODO
                message = "Document correctly deleted"
                AWSDocumentOperationResponseList.append(AWSDocumentOperationResponse(documentId, status, message))
            except:
                status = False
                message = "An error occured while deleting the document"
                AWSDocumentOperationResponseList.append(AWSDocumentOperationResponse(documentId, status, message))
        return AWSDocumentOperationResponseList

    def getDocumentsMetadata(self, documentFilter: str) -> List[AWSDocumentMetadata]:
        result = []
        awsDocumentMetadata = self.s3.list_objects_v2(Bucket=self.awsBucketName,
                                                      Prefix=documentFilter)
        contents = awsDocumentMetadata.get('Contents')
        for content in contents:
            awsMetadata = AWSDocumentMetadata(content.get('Key'),
                                            content.get('Size'),
                                            content.get('LastModified'))
            result.append(awsMetadata)
        return result


    def getDocumentContent(self, documentId: str) -> AWSDocument:
        aws = self.s3.get_object(Bucket=self.awsBucketName, Key=documentId)
        print(aws, flush=True)
        return AWSDocument(documentId,
                            aws.get('Body').read(),
                            aws.get('ContentType'),
                            aws.get('ContentLength'),
                            aws.get('LastModified'))
