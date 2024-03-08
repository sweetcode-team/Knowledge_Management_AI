from flask import request, Blueprint, jsonify
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from application.service.conceal_documents_service import ConcealDocumentsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager

concealDocumentsBlueprint = Blueprint("concealDocuments", __name__)

@concealDocumentsBlueprint.route("/concealDocuments", methods=['POST'])
def concealDocuments():
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())
    
    controller = ConcealDocumentsController(ConcealDocumentsService(configurationManager.getConcealDocumentsPort()))
    documentOperationResponses = controller.concealDocuments(request.json.get('ids'))
     
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])