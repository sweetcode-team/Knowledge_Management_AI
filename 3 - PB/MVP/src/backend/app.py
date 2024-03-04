from flask import Flask, request, jsonify
from flask_cors import CORS

from adapter._in.web.upload_documents_controller import UploadDocumentsController
from application.port.upload_documents_service import UploadDocumentsService
from application.port.documents_uploader import DocumentsUploader
from application.port.embeddings_uploader import EmbeddingsUploader

from adapter._in.web.new_document import NewDocument

app = Flask(__name__)
CORS(app)

@app.route("/uploadDocuments", methods=["POST"])
def uploadDocuments():

    uploadedDocuments = request.files['file']

    newDocuments = [
        NewDocument(
            documentId = uploadedDocument.filename,
            type = "PDF" if uploadedDocument.content_type == "application/pdf" else "DOCX",
            size = uploadedDocument.content_length,
            content = uploadedDocument.read()
        ) for uploadedDocument in uploadedDocuments
    ]

    controller = UploadDocumentsController(UploadDocumentsService(DocumentsUploader(), EmbeddingsUploader()))
    return jsonify(controller.uploadDocuments(newDocuments, True))