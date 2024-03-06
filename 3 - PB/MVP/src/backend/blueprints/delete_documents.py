from flask import request, Blueprint, jsonify
from adapter._in.web.delete_documents_controller import DeleteDocumentsController
from adapter.out.persistence.AWS_manager import AWSS3Manager
from application.port.delete_documents import DeleteDocuments 
from application.port.delete_documents_AWSS3 import DeleteDocumentsAWSS3
from application.port.delete_documents_embeddings import DeleteDocumentsEmbeddings
from application.port.delete_documents_service import DeleteDocumentsService
from application.port.delete_embeddings_vector_store import DeleteEmbeddingsVectorStore
from adapter.out.vector_store_pinecone_manager import VectorStorePineconeManager

deleteDocumentsBlueprint = Blueprint("deleteDocuments", __name__)

@deleteDocumentsBlueprint.route("/deleteDocuments", methods=['POST'])
def deleteDocuments():
    controller = DeleteDocumentsController(DeleteDocumentsService(DeleteDocuments(DeleteDocumentsAWSS3(AWSS3Manager()))), DeleteDocumentsEmbeddings(DeleteEmbeddingsVectorStore(VectorStorePineconeManager())))
    documentOperationResponses = controller.deleteDocuments(request.json.get('ids'))
     
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])