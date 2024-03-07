import os
from flask import request, Blueprint, jsonify, abort
from adapter._in.web.new_document import NewDocument
from adapter._in.web.upload_documents_controller import UploadDocumentsController
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from application.service.documents_uploader import DocumentsUploader
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from application.service.upload_documents_service import UploadDocumentsService
from application.service.embeddings_uploader import EmbeddingsUploader
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore
from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from werkzeug.utils import secure_filename

uploadDocumentsBlueprint = Blueprint("uploadDocuments", __name__)

@uploadDocumentsBlueprint.route("/uploadDocuments", methods=['POST'])
def uploadDocuments():
    # TODO: Add validation for the request
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

    controller = UploadDocumentsController(
        UploadDocumentsService(
            DocumentsUploader(
                DocumentsUploaderAWSS3(
                    AWSS3Manager()
                )
            ),
            EmbeddingsUploader(
                EmbeddingsUploaderFacadeLangchain(
                    Chunkerizer(),
                    EmbeddingsCreator(
                        HuggingFaceEmbeddingModel()
                    ),
                    EmbeddingsUploaderVectorStore(
                        VectorStoreChromaDBManager()
                    )
                )
            )
        )
    )
    documentOperationResponses = controller.uploadDocuments(newDocuments, False)
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])
