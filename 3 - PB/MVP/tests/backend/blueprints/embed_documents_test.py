from flask import request, Blueprint, jsonify
from adapter._in.web.embed_documents_controller import EmbedDocumentsController
from application.service.embed_documents_service import EmbedDocumentsService
from application.service.get_documents_content import GetDocumentsContent
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.get_documents_status import GetDocumentsStatus
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters

embedDocumentsBlueprint = Blueprint('embed_documents', __name__)

@embedDocumentsBlueprint.route('/embedDocuments', methods=['POST'])
def embedDocuments():
    requestedIds = request.form.getlist('documentIds')
    if requestedIds is None:
        raise InsufficientParameters()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())
    
    controller = EmbedDocumentsController(
        embedDocumentsUseCase = EmbedDocumentsService(
            GetDocumentsContent(configurationManager.getGetDocumentsContentPort()),
            EmbeddingsUploader(configurationManager.getEmbeddingsUploaderPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())
        )
    )
    
    documentOperationResponses = controller.embedDocuments(requestedIds)
    
    if len(documentOperationResponses) == 0:
        return jsonify("Errore nella generazione degli embeddings dei documenti."), 500
     
    return jsonify([{"id": documentOperationResponse.documentId.id, 
                     "status": documentOperationResponse.status, 
                     "message": documentOperationResponse.message} 
                    for documentOperationResponse in documentOperationResponses])