import os
from flask import request, Blueprint, jsonify, abort
from werkzeug.utils import secure_filename
from adapter._in.web.new_document import NewDocument
from adapter._in.web.upload_documents_controller import UploadDocumentsController
from application.service.upload_documents_service import UploadDocumentsService
from application.service.documents_uploader import DocumentsUploader
from application.service.embeddings_uploader import EmbeddingsUploader

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager


uploadDocumentsBlueprint = Blueprint("uploadDocuments", __name__)

@uploadDocumentsBlueprint.route("/uploadDocuments", methods=['POST'])
def uploadDocuments():
    newDocuments = []

    for uploadedDocument in request.files.getlist('documents'):
        filename = secure_filename(uploadedDocument.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext.lower() not in [".pdf", ".docx"]:
                abort(400, f"Il documento {uploadedDocument.filename} non è supportato.")

            contentType = uploadedDocument.content_type
            if contentType == "application/pdf" or contentType == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                newDocument = NewDocument(
                    documentId = uploadedDocument.filename,
                    type = "PDF" if contentType == "application/pdf" else "DOCX",
                    size = uploadedDocument.content_length,
                    content = uploadedDocument.read()
                )
                newDocuments.append(newDocument)
        else:
            abort(400, "L'upload di documenti senza titolo non è supportato.")

    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = UploadDocumentsController(
        upload_documents_use_case=UploadDocumentsService(
            DocumentsUploader(configurationManager.getDocumentsUploaderPort()),
            EmbeddingsUploader(configurationManager.getEmbeddingsUploaderPort())
        )
    )
    documentOperationResponses = controller.uploadDocuments(newDocuments, False)
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])
