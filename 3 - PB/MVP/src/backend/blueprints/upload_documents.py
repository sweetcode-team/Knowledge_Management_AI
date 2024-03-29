import os
from flask import request, Blueprint, jsonify
from werkzeug.utils import secure_filename
from adapter._in.web.presentation_domain.new_document import NewDocument
from adapter._in.web.upload_documents_controller import UploadDocumentsController
from application.service.upload_documents_service import UploadDocumentsService
from application.service.documents_uploader import DocumentsUploader
from application.service.embeddings_uploader import EmbeddingsUploader

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager

from api_exceptions import InsufficientParameters, DocumentNotSupported, APIElaborationException

uploadDocumentsBlueprint = Blueprint("uploadDocuments", __name__)

"""
This method is the endpoint for the uploadDocuments API.
Returns:
    jsonify: The response of the API.
"""
@uploadDocumentsBlueprint.route("/uploadDocuments", methods=['POST'])
def uploadDocuments():
    forceUpload = request.form.get('forceUpload')
    if forceUpload is None:
        forceUpload = False
    
    newDocuments = []
    for uploadedDocument in request.files.getlist('documents'):
        secureFilename = secure_filename(uploadedDocument.filename)
        if secureFilename == '':
            raise DocumentNotSupported("L'upload di documenti senza titolo non è supportato.")
        
        contentType = uploadedDocument.content_type
        if contentType == "application/pdf" or contentType == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            newDocument = NewDocument(
                documentId = secureFilename,
                type = "PDF" if contentType == "application/pdf" else "DOCX",
                size = uploadedDocument.content_length,
                content = uploadedDocument.read()
            )
            newDocuments.append(newDocument)
        else:
            raise DocumentNotSupported(f"Documento {uploadedDocument.filename} non supportato.")
            
    if len(newDocuments) == 0:
        raise InsufficientParameters()

    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = UploadDocumentsController(
        uploadDocumentsUseCase = UploadDocumentsService(
            DocumentsUploader(configurationManager.getDocumentsUploaderPort()),
            EmbeddingsUploader(configurationManager.getEmbeddingsUploaderPort())
        )
    )
    
    documentOperationResponses = controller.uploadDocuments(newDocuments, forceUpload)
    
    if len(documentOperationResponses) == 0:
        raise APIElaborationException("Errore nell'upload dei documenti.")
        
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.ok(),
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])
