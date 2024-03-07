from flask import request, Blueprint, jsonify
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from application.service.conceal_documents_service import ConcealDocumentsService
from adapter.out.conceal_documents.conceal_documents_vector_store import ConcealDocumentsVectorStore
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

concealDocumentsBlueprint = Blueprint("concealDocuments", __name__)

@concealDocumentsBlueprint.route("/concealDocuments", methods=['POST'])
def concealDocuments():
    controller = ConcealDocumentsController(ConcealDocumentsService(ConcealDocumentsVectorStore(VectorStorePineconeManager())))
    documentOperationResponses = controller.concealDocuments(request.json.get('ids'))
     
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])