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

from api_exceptions import DocumentNotSupported
from api_exceptions import InsufficientParameters

uploadDocumentsBlueprint = Blueprint("uploadDocuments", __name__)

@uploadDocumentsBlueprint.route("/uploadDocuments", methods=['POST'])
def uploadDocuments():
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
    
    # TODO: forceUpload = False qui, in Substitute mettere True
    documentOperationResponses = controller.uploadDocuments(newDocuments, False)
    
    if len(documentOperationResponses) == 0:
        return jsonify("Errore nell'upload dei documenti."), 500
        
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.status,
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])
