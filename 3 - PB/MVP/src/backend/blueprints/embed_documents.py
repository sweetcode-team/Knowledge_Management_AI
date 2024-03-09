from flask import request, Blueprint, jsonify
from adapter._in.web.embed_documents_controller import EmbedDocumentsController
from application.service.embed_documents_service import EmbedDocumentsService
from application.service.get_documents_content import GetDocumentsContent
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.get_documents_status import GetDocumentsStatus
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager

embedDocumentsBlueprint = Blueprint('embed_documents', __name__)

@embedDocumentsBlueprint.route('/embedDocuments', methods=['POST'])
def embedDocuments():
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())
    
    controller = EmbedDocumentsController(
        embedDocumentsUseCase = EmbedDocumentsService(
            GetDocumentsContent(configurationManager.getGetDocumentsContentPort()),
            EmbeddingsUploader(configurationManager.getEmbeddingsUploaderPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())))
    
    documentOperationResponses = controller.embedDocuments(request.json.get('ids'))
     
    return jsonify([{"id": documentOperationResponse.documentId.id, 
                     "status": documentOperationResponse.status, 
                     "message": documentOperationResponse.message} 
                    for documentOperationResponse in documentOperationResponses])