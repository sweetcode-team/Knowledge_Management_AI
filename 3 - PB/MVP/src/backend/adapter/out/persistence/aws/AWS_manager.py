from typing import List

import boto3
from adapter.out.persistence.aws.AWS_document import AWSDocument
from adapter.out.persistence.aws.AWS_document_operation_response import AWSDocumentOperationResponse
from adapter.out.persistence.aws.AWS_document_metadata import AWSDocumentMetadata

from botocore.exceptions import ClientError

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

    """
    Get the document from the S3 bucket by its ID.
    Args:
        documentId (str): The ID of the document to get.
    Returns:
        AWSDocument: The document from the S3 bucket.
    """
    def getDocumentById(self, documentId: str) -> AWSDocument:
        try:
            aws = self.s3.get_object(Bucket=self.awsBucketName, Key=documentId)
            id = aws.get('Key')
            content = aws.get('Body').read()
            type = aws.get('ContentType')
            size = aws.get('ContentLength')
            uploadTime = aws.get('LastModified')
        except Exception as e:
            return None
        return AWSDocument(
            id=id,
            content=content,
            type=type,
            size=size,
            uploadTime=uploadTime
        )

    """
    Upload the documents to the S3 bucket.
    Args:
        awsDocuments (List[AWSDocument]): The documents to upload.
        forceUpload (bool): The flag to force the upload of the documents.
    Returns:
        List[AWSDocumentOperationResponse]: The response of the upload operation.
    """
    def uploadDocuments(self, awsDocuments: List[AWSDocument], forceUpload: bool) -> List[AWSDocumentOperationResponse]:
        AWSDocumentOperationResponses = []

        if not forceUpload:
            for awsDocument in awsDocuments:
                try:
                    self.s3.head_object(Bucket=self.awsBucketName, Key=awsDocument.id)
                    # The document is already present in the system, so it cannot be uploaded.
                    AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(awsDocument.id, False, "Il documento è già presente nel sistema."))
                except Exception as e:
                    # The document is not present in the system, so it can be uploaded.
                    try:
                        self.s3.put_object(Bucket=self.awsBucketName, Key=awsDocument.id, Body=awsDocument.content, ContentType=awsDocument.type)
                        AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(awsDocument.id, True, "Caricamento del documento avvenuto con successo."))
                    except Exception as e:
                        # An error occurred during the put_object operation.
                        AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(awsDocument.id, False, f"Errore durante il caricamento del documento: {e}"))
                    continue
        else:
            # The forceUpload flag is set to True, so the documents can be uploaded without checking if they are already present in the system.
            for awsDocument in awsDocuments:
                try:
                    self.s3.put_object(Bucket=self.awsBucketName, Key=awsDocument.id, Body=awsDocument.content, ContentType=awsDocument.type)
                    AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(awsDocument.id, True, "Caricamento del documento avvenuto con successo."))
                except Exception as e:
                    # An error occurred during the put_object operation.
                    AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(awsDocument.id, False, f"Errore durante il caricamento del documento: {e}"))
                    continue
            
        return AWSDocumentOperationResponses

    """
    Delete the documents from the S3 bucket.
    Args:
        documentsIds (List[str]): The documents to delete.
    Returns:
        List[AWSDocumentOperationResponse]: The response of the delete operation.
    """
    def deleteDocuments(self, documentsIds: List[str]) -> List[AWSDocumentOperationResponse]:
        AWSDocumentOperationResponses = []

        for documentId in documentsIds:
            try:
                self.s3.delete_object(Bucket=self.awsBucketName, Key=documentId)
                AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(documentId, True, "Eliminazione del documento avvenuta con successo."))
            except ClientError as e:
                if e.response['Error']['Code'] == 'NoSuchKey':
                    AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(documentId, False, "Il documento non è presente nel sistema."))
                else:
                    AWSDocumentOperationResponses.append(AWSDocumentOperationResponse(documentId, False, f"Errore durante l'eliminazione del documento: {e}"))
                continue

        return AWSDocumentOperationResponses

    """
    Get the metadata of the documents from the S3 bucket.
    Args:
        documentFilter (str): The filter to apply to the documents.
    Returns:
        List[AWSDocumentMetadata]: The metadata of the documents from the S3 bucket.
    """
    def getDocumentsMetadata(self, documentFilter: str) -> List[AWSDocumentMetadata]:
        awsDocumentsMetadata = []
        documentMetadataResponse = self.s3.list_objects_v2(Bucket=self.awsBucketName, Prefix=documentFilter)
        contents = documentMetadataResponse.get('Contents', [])
        for content in contents:
            awsDocumentsMetadata.append(
                AWSDocumentMetadata(
                    id=content.get('Key'),
                    size=content.get('Size'),
                    uploadTime=content.get('LastModified'),
                )
            )
        return awsDocumentsMetadata

    """
    Get the document content from the S3 bucket by its ID.
    Args:
        documentId (str): The ID of the document to get the content.
    Returns:
        AWSDocument: The document content from the S3 bucket.
    """
    def getDocumentContent(self, documentId: str) -> AWSDocument:
        try:
            documentContentResponse = self.s3.get_object(Bucket=self.awsBucketName, Key=documentId)
            return AWSDocument(
                id=documentId,
                content=documentContentResponse.get('Body').read(),
                type=documentContentResponse.get('ContentType'),
                size=documentContentResponse.get('ContentLength'),
                uploadTime=documentContentResponse.get('LastModified')
            )
        except Exception as e:
            return None