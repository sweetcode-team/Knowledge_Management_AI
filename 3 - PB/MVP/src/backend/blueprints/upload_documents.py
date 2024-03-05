from adapter._in.web.new_document import NewDocument
from adapter._in.web.upload_documents_controller import UploadDocumentsController
from adapter.out.persistence.AWS_manager import AWSS3Manager
from application.port.documents_uploader import DocumentsUploader
from application.port.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from application.port.embeddings_uploader import EmbeddingsUploader
from application.port.upload_documents_service import UploadDocumentsService
from flask import request, Blueprint, jsonify

uploadDocumentsBlueprint = Blueprint("uploadDocuments", __name__)
"""
    This class is responsible for managing the upload of documents.
    Methods:
        uploadDocuments() -> List[DocumentOperationResponse]:
            Upload the documents to the S3 bucket.
"""
@uploadDocumentsBlueprint.route("/uploadDocuments", methods=['POST'])
def uploadDocuments():
    newDocuments = [
        NewDocument(
            documentId = uploadedDocument.filename,
            type = "PDF" if uploadedDocument.content_type == "application/pdf" else "DOCX",
            size = uploadedDocument.content_length,
            content = uploadedDocument.read()
        ) for uploadedDocument in request.files.getlist('file')
    ]
    controller = UploadDocumentsController(UploadDocumentsService(DocumentsUploader(DocumentsUploaderAWSS3(AWSS3Manager())), EmbeddingsUploader()))
    documentOperationResponses = controller.uploadDocuments(newDocuments, False)
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])