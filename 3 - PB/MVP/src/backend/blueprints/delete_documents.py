from flask import request, Blueprint, jsonify
from adapter._in.web.delete_documents_controller import DeleteDocumentsController
from application.service.delete_documents_service import DeleteDocumentsService
from application.service.delete_documents import DeleteDocuments
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters

deleteDocumentsBlueprint = Blueprint("deleteDocuments", __name__)

@deleteDocumentsBlueprint.route("/deleteDocuments", methods=['POST'])
def deleteDocuments():
    requestedIds = request.form.get('documentIds')
    if requestedIds is None:
        raise InsufficientParameters()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = DeleteDocumentsController(DeleteDocumentsService(DeleteDocuments(configurationManager.getDeleteDocumentsPort()), DeleteDocumentsEmbeddings(configurationManager.getDeleteEmbeddingsPort())))
    
    documentOperationResponses = controller.deleteDocuments(requestedIds)
     
    if len(documentOperationResponses) == 0:
        return jsonify("Errore nell'eliminazione dei documenti."), 500
    
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.status,
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])