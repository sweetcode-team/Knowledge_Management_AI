from flask import request, Blueprint, jsonify
from adapter._in.web.enable_documents_controller import EnableDocumentsController
from adapter.out.enable_documents.enable_documents_vector_store import EnableDocumentsVectorStore
from application.service.enable_documents_service import EnableDocumentsService
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

enableDocumentsBlueprint = Blueprint("enableDocuments", __name__)

@enableDocumentsBlueprint.route("/enableDocuments", methods=['POST'])
def enableDocuments():
    controller = EnableDocumentsController(
        EnableDocumentsService(
            EnableDocumentsVectorStore(
                VectorStorePineconeManager())))
    documentOperationResponses = controller.enableDocuments(request.json.get('ids'))
     
    return jsonify([{"id": documentOperationResponse.documentId.id, 
                     "status": documentOperationResponse.status, 
                     "message": documentOperationResponse.message} 
                    for documentOperationResponse in documentOperationResponses])