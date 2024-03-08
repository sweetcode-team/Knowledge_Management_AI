from flask import request, Blueprint, jsonify
from adapter._in.web.enable_documents_controller import EnableDocumentsController
from application.service.enable_documents_service import EnableDocumentsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager

enableDocumentsBlueprint = Blueprint("enableDocuments", __name__)

@enableDocumentsBlueprint.route("/enableDocuments", methods=['POST'])
def enableDocuments():
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = EnableDocumentsController(EnableDocumentsService(configurationManager.getEnableDocumentsPort()))
    documentOperationResponses = controller.enableDocuments(request.json.get('ids'))
    
    return jsonify([{"id": documentOperationResponse.documentId.id, "status": documentOperationResponse.status, "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])