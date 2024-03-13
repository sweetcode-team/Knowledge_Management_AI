from flask import Blueprint, jsonify

from adapter._in.web.get_documents_controller import GetDocumentsController
from application.service.get_documents_facade_service import GetDocumentsFacadeService
from application.service.get_documents_metadata import GetDocumentsMetadata
from application.service.get_documents_status import GetDocumentsStatus

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters, APIBadRequest

getDocumentsBlueprint = Blueprint("getDocuments", __name__)

@getDocumentsBlueprint.route('/getDocuments', defaults={'filter': ''}, methods=['GET'])
@getDocumentsBlueprint.route("/getDocuments/<filter>", methods=['GET'])
def getDocuments(filter):
    if filter is None:
        raise InsufficientParameters()
    validFilter = filter.strip()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = GetDocumentsController(
        GetDocumentsFacadeService(
            GetDocumentsMetadata(configurationManager.getGetDocumentsMetadataPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())
        )
    )
    
    documents = controller.getDocuments(validFilter)
    
    if len(documents) == 0:
        return jsonify([]), 404
    
    return jsonify([{
        "id": document.metadata.id.id,
        "type": document.metadata.type.name,
        "size": document.metadata.size,
        "uploadDate": document.metadata.uploadTime,
        "status": document.status.status.name} for document in documents])