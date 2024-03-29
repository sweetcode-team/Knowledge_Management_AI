from flask import request, Blueprint, jsonify
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from application.service.conceal_documents_service import ConcealDocumentsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import APIBadRequest, InsufficientParameters, APIElaborationException

concealDocumentsBlueprint = Blueprint("concealDocuments", __name__)

"""
This method is the endpoint for the concealDocuments API.
Returns:
    jsonify: The response of the API.
"""  
@concealDocumentsBlueprint.route("/concealDocuments", methods=['POST'])  
def concealDocuments():
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
            validDocumentIds.append(requestedId.strip())
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())
    
    controller = ConcealDocumentsController(ConcealDocumentsService(configurationManager.getConcealDocumentsPort()))
    
    documentOperationResponses = controller.concealDocuments(validDocumentIds)
    
    if len(documentOperationResponses) == 0:
        raise APIElaborationException("Errore nell'occultamento dei documenti.")
    
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.ok(),
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])