from flask import request, Blueprint, jsonify
from adapter._in.web.enable_documents_controller import EnableDocumentsController
from application.service.enable_documents_service import EnableDocumentsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters, APIBadRequest, APIElaborationException

enableDocumentsBlueprint = Blueprint("enableDocuments", __name__)

@enableDocumentsBlueprint.route("/enableDocuments", methods=['POST'])
def enableDocuments():
    requestedIds = request.form.getlist('documentIds')
    if requestedIds is None:
        raise InsufficientParameters()
    if len(requestedIds) == 0:
        raise APIBadRequest("Nessun id di documento specificato.")
    validDocumentIds = []
    for requestedId in requestedIds:
        if requestedId.strip() == "":
            raise APIBadRequest(f"Id di documento '{requestedId}' non valido.")
        else:
            validDocumentIds.append((requestedId).strip())
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = EnableDocumentsController(EnableDocumentsService(configurationManager.getEnableDocumentsPort()))
    
    documentOperationResponses = controller.enableDocuments(validDocumentIds)
    
    if len(documentOperationResponses) == 0:
        raise APIElaborationException("Errore nella riabilitazione dei documenti.")
    
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.status,
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])