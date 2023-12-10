import os
import shutil
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from config import STORAGE_FOLDER

class DocumentManager:
    """Manages document-related operations.

    This class provides methods for handling document-related tasks such as folder management,
    PDF to document conversion, and chunking of text documents.

    Attributes:
        None

    Methods:
        delete_folder(upload_folder):
            Deletes the specified folder and its contents.

        configure_upload_folder():
            Configures and returns the upload folder path.

        pdf_to_documents(pdf_file, upload_folder):
            Converts a PDF file to a list of documents.

        get_docs_chunks(documents, chunk_size, chunk_overlap):
            Splits a list of documents into chunks of specified size with an optional overlap.
    """

    @staticmethod
    def delete_folder(upload_folder):
        """Delete the specified folder and its contents.

        Args:
            upload_folder (str): The path of the folder to be deleted.

        Returns:
            None
        """
        if os.path.exists(upload_folder):
            shutil.rmtree(upload_folder)

    @staticmethod
    def configure_upload_folder():
        """Configure and return the upload folder path.

        The upload folder is determined based on the STORAGE_FOLDER configuration.

        Args:
            None

        Returns:
            str: The path of the configured upload folder.
        """
        path = os.path.dirname(os.path.abspath(__file__))
        upload_folder = os.path.join(path, STORAGE_FOLDER)
        os.makedirs(upload_folder, exist_ok=True)
        return upload_folder

    @staticmethod
    def pdf_to_documents(pdf_file, upload_folder):
        """Convert a PDF file to a list of documents.

        This method saves the PDF file to the specified upload folder and extracts
        individual documents from the PDF.

        Args:
            pdf_file (FileStorage): The uploaded PDF file.
            upload_folder (str): The path of the upload folder.

        Returns:
            tuple: A tuple containing a list of documents and the path to the saved PDF file.
        """
        save_path = os.path.join(upload_folder, pdf_file.filename)
        pdf_file.save(save_path)
        pdf = PyPDFLoader(save_path)
        documents = pdf.load()
        for document in documents:
            document.metadata["file_name"] = pdf_file.filename[:-4]
        return documents, save_path

    @staticmethod
    def get_docs_chunks(documents, chunk_size, chunk_overlap):
        """Split a list of documents into chunks of specified size with optional overlap.

        This method uses the CharacterTextSplitter to divide the text content of
        each document into chunks of the specified size, with an optional overlap.

        Args:
            documents (list): A list of documents.
            chunk_size (int): The size of each chunk.
            chunk_overlap (int): The overlap between consecutive chunks.

        Returns:
            list: A list of chunks, each containing text content from the documents.
        """
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(documents)
