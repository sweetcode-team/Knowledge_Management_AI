from flask import request, Blueprint, jsonify

from adapter._in.web.get_documents_controller import GetDocumentsController
from application.service.get_documents_facade_service import GetDocumentsFacadeService
from application.service.get_documents_metadata import GetDocumentsMetadata
from application.service.get_documents_status import GetDocumentsStatus

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager

getDocumentsBlueprint = Blueprint("getDocuments", __name__)


@getDocumentsBlueprint.route("/getDocuments", methods=['POST'])
def getDocuments():
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = GetDocumentsController(
        GetDocumentsFacadeService(
            GetDocumentsMetadata(configurationManager.getGetDocumentsMetadataPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())
        )
    )
    
    documentOperationResponses = controller.getDocuments(request.json.get('filter'))
    return jsonify([{"id": documentOperationResponse.metadata.id.id,
                    "type": documentOperationResponse.metadata.type.name,
                    "size": documentOperationResponse.metadata.size,
                    "uploadDate": documentOperationResponse.metadata.uploadTime,
                    "status": documentOperationResponse.status.status.name} for documentOperationResponse in documentOperationResponses])