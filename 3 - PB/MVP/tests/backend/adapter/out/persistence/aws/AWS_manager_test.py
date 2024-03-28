from unittest.mock import MagicMock, patch, ANY, mock_open
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager

def test_getDocumentById():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocument') as AWSDocumentMock:
                
            s3Mock = MagicMock()
            awsMock = MagicMock()
            
            boto3Mock.client.return_valuee = s3Mock
            s3Mock.get_object.return_value = awsMock  
                
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.getDocumentById("Prova.pdf")

            assert response == AWSDocumentMock.return_value    

def test_uploadDocumentsFalsePresent():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            AWSDocumentMock = MagicMock() 
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.uploadDocuments([AWSDocumentMock], False)
            
            s3Mock.head_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id)
            s3Mock.put_object.assert_not_called()
            AWSDocumentOperationResponseMock.assert_called_once_with(AWSDocumentMock.id, False, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value
            
def test_uploadDocumentsFalseNotPresentTrue():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            AWSDocumentMock = MagicMock() 
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            s3Mock.head_object.side_effect = Exception
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.uploadDocuments([AWSDocumentMock], False)
            
            s3Mock.head_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id)
            s3Mock.put_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id, Body=AWSDocumentMock.content)
            AWSDocumentOperationResponseMock.assert_called_once_with(AWSDocumentMock.id, True, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value
            
def test_uploadDocumentsFalseNotPresentFalse():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            AWSDocumentMock = MagicMock() 
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            s3Mock.head_object.side_effect = Exception
            s3Mock.put_object.side_effect = Exception
            
            awsS3Manager = AWSS3Manager() 

            response = awsS3Manager.uploadDocuments([AWSDocumentMock], False)
            
            s3Mock.head_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id)
            s3Mock.put_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id, Body=AWSDocumentMock.content)
            AWSDocumentOperationResponseMock.assert_called_once_with(AWSDocumentMock.id, False, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value
            
def test_uploadDocumentsTrueTrue():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            AWSDocumentMock = MagicMock() 
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.uploadDocuments([AWSDocumentMock], True)
            
            s3Mock.head_object.assert_not_called()
            s3Mock.put_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id, Body=AWSDocumentMock.content)
            AWSDocumentOperationResponseMock.assert_called_once_with(AWSDocumentMock.id, True, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value 
            
def test_uploadDocumentsTrueFail():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            AWSDocumentMock = MagicMock() 
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            s3Mock.put_object.side_effect = Exception
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.uploadDocuments([AWSDocumentMock], True)
            
            s3Mock.head_object.assert_not_called()
            s3Mock.put_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key=AWSDocumentMock.id, Body=AWSDocumentMock.content)
            AWSDocumentOperationResponseMock.assert_called_once_with(AWSDocumentMock.id, False, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value

def test_deleteDocumentsTrue():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.deleteDocuments(["Prova.pdf"])
            
            s3Mock.delete_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key="Prova.pdf")
            AWSDocumentOperationResponseMock.assert_called_once_with("Prova.pdf", True, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value
            
def test_deleteDocumentsFail():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            from botocore.exceptions import ClientError
            s3Mock.delete_object.side_effect = ClientError({'Error': {'Code': 'test', 'Message': 'test'}}, 'delete_object')
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.deleteDocuments(["Prova.pdf"])
            
            s3Mock.delete_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key="Prova.pdf")
            AWSDocumentOperationResponseMock.assert_called_once_with("Prova.pdf", False, ANY)
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value  
            
def test_deleteDocumentsNotFound():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentOperationResponse') as AWSDocumentOperationResponseMock:
            
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            from botocore.exceptions import ClientError
            s3Mock.delete_object.side_effect = ClientError({'Error': {'Code': 'NoSuchKey', 'Message': 'test'}}, 'delete_object')
            
            awsS3Manager = AWSS3Manager()

            response = awsS3Manager.deleteDocuments(["Prova.pdf"])
            
            s3Mock.delete_object.assert_called_once_with(Bucket=awsS3Manager.awsBucketName, Key="Prova.pdf")
            AWSDocumentOperationResponseMock.assert_called_once_with("Prova.pdf", False, "Il documento non è presente nel sistema.")
            assert isinstance(response, list)
            assert response[0] == AWSDocumentOperationResponseMock.return_value
            
def test_getDocumentsMetadataWithFilter():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentMetadata') as AWSDocumentMetadataMock:
            
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            s3Mock.list_objects_v2.return_value = {'Contents': [{'Key': 'Prova.pdf', 'LastModified': '2021-05-21T14:00:00Z', 'Size': 100, 'ContentType': 'pdf'}]}
            
            awsS3Manager = AWSS3Manager()
            
            response = awsS3Manager.getDocumentsMetadata(documentFilter = "test_filter")
            
            AWSDocumentMetadataMock.assert_called_once_with(id='Prova.pdf', size=100, uploadTime='2021-05-21T14:00:00Z')
            assert isinstance(response, list)
            assert response[0] == AWSDocumentMetadataMock.return_value
            
def test_getDocumentsMetadataWithoutFilter():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocumentMetadata') as AWSDocumentMetadataMock:
            
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            s3Mock.list_objects_v2.return_value = {'Contents': [{'Key': 'Prova.pdf', 'LastModified': '2021-05-21T14:00:00Z', 'Size': 100, 'ContentType': 'pdf'}]}
            
            awsS3Manager = AWSS3Manager()
            
            response = awsS3Manager.getDocumentsMetadata(documentFilter = "")
            
            AWSDocumentMetadataMock.assert_called_once_with(id='Prova.pdf', size=100, uploadTime='2021-05-21T14:00:00Z')
            assert isinstance(response, list)
            assert response[0] == AWSDocumentMetadataMock.return_value
            
def test_getDocumentContentTrue():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocument') as AWSDocumentMock:
            
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            
            awsS3Manager = AWSS3Manager()
            
            response = awsS3Manager.getDocumentContent("Prova.pdf")
            
            AWSDocumentMock.assert_called_once()
            assert response == AWSDocumentMock.return_value
            
def test_getDocumentContentFail():
    with    patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.AWSDocument') as AWSDocumentMock:
            s3Mock = MagicMock()
            
            boto3Mock.client.return_value = s3Mock
            s3Mock.get_object.side_effect = Exception
            
            awsS3Manager = AWSS3Manager()
            
            response = awsS3Manager.getDocumentContent("Prova.pdf")
            
            AWSDocumentMock.assert_not_called()
            assert response == None