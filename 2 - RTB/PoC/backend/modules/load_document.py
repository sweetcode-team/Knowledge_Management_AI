import logging
import os
import boto3

class FileStore:
    """A class for interacting with an AWS S3 bucket for file storage."""

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, bucket_name):
        """
        Initializes a new FileStore instance.

        Args:
            aws_access_key_id (str): The AWS access key ID.
            aws_secret_access_key (str): The AWS secret access key.
            region_name (str): The AWS region name.
            bucket_name (str): The name of the S3 bucket to be used.

        Returns:
            None
        """
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.region_name = region_name
        self.bucket_name = bucket_name
        self.set_bucket(self.bucket_name)

    def buckets_list(self):
        """
        Lists all S3 buckets in the AWS account.

        Returns:
            list: A list of strings containing the names of S3 buckets.
                  Returns None if an error occurs during the operation.
        """
        buckets = []
        try:
            response = self.s3_client.list_buckets()
            if response:
                for bucket in response['Buckets']:
                    buckets.append(f"{bucket['Name']}")
        except Exception as e:
            logging.error(e)
            return None
        return buckets

    def set_bucket(self, bucket_name):
        """
        Sets the current S3 bucket for file operations.

        Args:
            bucket_name (str): The name of the S3 bucket to be set.

        Returns:
            bool: True if the bucket is set successfully, False otherwise.
        """
        try:
            location = {'LocationConstraint': self.region_name}
            if bucket_name not in self.buckets_list():
                self.s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        except Exception as e:
            logging.error(e)
            return False
        self.bucket_name = bucket_name
        return True

    def upload_file(self, file_path, file_name):
        """
        Uploads a file to the current S3 bucket.

        Args:
            file_path (str): The local path of the file to be uploaded.
            file_name (str): The name to be given to the file in the S3 bucket.

        Returns:
            bool: True if the file is uploaded successfully, False otherwise.
        """
        # If file_path not specified, use file_name
        if file_path is None:
            file_path = os.path.basename(file_name)

        try:
            self.s3_client.upload_file(Filename=file_path, Bucket=self.bucket_name, Key=file_name)
        except Exception as e:
            print(e)
            return False
        return True

    def download_file(self, file_name, destination_file_path):
        """
        Downloads a file from the current S3 bucket to a local destination.

        Args:
            file_name (str): The name of the file in the S3 bucket.
            destination_file_path (str): The local path to save the downloaded file.

        Returns:
            bool: True if the file is downloaded successfully, False otherwise.
        """
        try:
            self.s3_client.download_file(Bucket=self.bucket_name, Key=file_name, Filename=destination_file_path)
        except Exception as e:
            logging.error(e)
            return False
        return True

    def delete_file(self, file_name):
        """
        Deletes a file from the current S3 bucket.

        Args:
            file_name (str): The name of the file to be deleted.

        Returns:
            bool: True if the file is deleted successfully, False otherwise.
        """
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_name)
        except Exception as e:
            logging.error(e)
            return False
        return True

    def delete_bucket(self, bucket_name):
        """
        Deletes an S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket to be deleted.

        Returns:
            bool: True if the bucket is deleted successfully, False otherwise.
        """
        try:
            self.s3_client.delete_bucket(Bucket=bucket_name)
        except Exception as e:
            logging.error(e)
            return False
        return True
    