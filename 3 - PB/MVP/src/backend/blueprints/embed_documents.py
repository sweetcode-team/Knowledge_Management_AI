from flask import request, Blueprint, jsonify
from adapter._in.web.embed_documents_controller import EmbedDocumentsController
from application.service.embed_documents_service import EmbedDocumentsService
from application.service.get_documents_content import GetDocumentsContent
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.get_documents_status import GetDocumentsStatus
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters, APIBadRequest, APIElaborationException

embedDocumentsBlueprint = Blueprint('embed_documents', __name__)

"""
This method is the endpoint for the embedDocuments API.
Returns:
    jsonify: The response of the API.
"""
@embedDocumentsBlueprint.route('/embedDocuments', methods=['POST'])
def embedDocuments():
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
    
    controller = EmbedDocumentsController(
        embedDocumentsUseCase = EmbedDocumentsService(
            GetDocumentsContent(configurationManager.getGetDocumentsContentPort()),
            EmbeddingsUploader(configurationManager.getEmbeddingsUploaderPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())
        )
    )
    
    documentOperationResponses = controller.embedDocuments(validDocumentIds)
    
    if len(documentOperationResponses) == 0:
        raise APIElaborationException("Errore nella generazione degli embeddings dei documenti.")
     
    return jsonify([{"documentId": documentOperationResponse.documentId.id,
                     "status": documentOperationResponse.ok(), 
                     "message": documentOperationResponse.message} 
                    for documentOperationResponse in documentOperationResponses])