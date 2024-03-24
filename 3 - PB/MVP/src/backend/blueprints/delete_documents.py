from flask import request, Blueprint, jsonify
from adapter._in.web.delete_documents_controller import DeleteDocumentsController
from application.service.delete_documents_service import DeleteDocumentsService
from application.service.delete_documents import DeleteDocuments
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters, APIBadRequest, APIElaborationException

deleteDocumentsBlueprint = Blueprint("deleteDocuments", __name__)

"""
This method is the endpoint for the deleteDocuments API.
Returns:
    jsonify: The response of the API.
"""
@deleteDocumentsBlueprint.route("/deleteDocuments", methods=['POST'])
def deleteDocuments():
    requestedIds = request.form.getlist('documentIds')
    print(requestedIds, flush=True)
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

    controller = DeleteDocumentsController(
        DeleteDocumentsService(
            DeleteDocuments(configurationManager.getDeleteDocumentsPort()),
            DeleteDocumentsEmbeddings(configurationManager.getDeleteEmbeddingsPort())
        )
    )
    
    documentOperationResponses = controller.deleteDocuments(validDocumentIds)
     
    if len(documentOperationResponses) == 0:
        raise APIElaborationException("Errore nell'eliminazione dei documenti.")
    
    return jsonify([{
        "id": documentOperationResponse.documentId.id,
        "status": documentOperationResponse.ok(),
        "message": documentOperationResponse.message} for documentOperationResponse in documentOperationResponses])