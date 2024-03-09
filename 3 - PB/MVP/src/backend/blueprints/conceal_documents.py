from flask import request, Blueprint, jsonify
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from application.service.conceal_documents_service import ConcealDocumentsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters

concealDocumentsBlueprint = Blueprint("concealDocuments", __name__)

@concealDocumentsBlueprint.route("/concealDocuments", methods=['POST'])
def concealDocuments():
    requestedIds = request.form.get('documentIds')
    if requestedIds is None:
        raise InsufficientParameters()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())
    
    controller = ConcealDocumentsController(ConcealDocumentsService(configurationManager.getConcealDocumentsPort()))
    
    documentOperationResponses = controller.concealDocuments(requestedIds)
    
    if len(documentOperationResponses) == 0:
        return jsonify("Errore nell'occultamento dei documenti."), 500
    
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.status,
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])