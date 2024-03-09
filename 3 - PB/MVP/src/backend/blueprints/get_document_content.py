from flask import Blueprint, jsonify
from adapter._in.web.get_document_content_controller import GetDocumentContentController
from application.service.get_documents_content_facade_service import GetDocumentsContentFacadeService
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_content import GetDocumentsContent

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters

getDocumentContentBlueprint = Blueprint("getDocumentContent", __name__)

@getDocumentContentBlueprint.route("/getDocumentContent/<int:documentId>", methods=['GET'])
def getDocumentsContent(documentId):
    if documentId is None:
        raise InsufficientParameters()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = GetDocumentContentController(
        GetDocumentsContentFacadeService(
            GetDocumentsContent(configurationManager.getGetDocumentsContentPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())
        )
    )
    
    retrievedDocument = controller.getDocumentContent(documentId)
    
    if retrievedDocument is None or retrievedDocument.plainDocument is None:
        return jsonify({}), 404
    
    return jsonify({
        "id": retrievedDocument.plainDocument.metadata.id.id,
        "content": retrievedDocument.plainDocument.content.content.hex(),
        "type": retrievedDocument.plainDocument.metadata.type.name,
        "size": retrievedDocument.plainDocument.metadata.size,
        "uploadDate": retrievedDocument.plainDocument.metadata.uploadTime,
        "status": retrievedDocument.documentStatus.status.name
    })