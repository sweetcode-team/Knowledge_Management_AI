from flask import request, Blueprint, jsonify

from adapter._in.web.get_document_content_controller import GetDocumentContentController
from application.service.get_document_content_facade_service import GetDocumentContentFacadeService
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_content import GetDocumentsContent
from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager

getDocumentContentBlueprint = Blueprint("getDocumentContent", __name__)


@getDocumentContentBlueprint.route("/getDocumentContent", methods=['POST'])
def getDocumentsContent():
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = GetDocumentContentController(
        GetDocumentContentFacadeService(
            GetDocumentsContent(configurationManager.getGetDocumentsContentPort()),
            GetDocumentsStatus(configurationManager.getGetDocumentsStatusPort())
        )
    )
    
    documentOperationResponses = controller.getDocumentContent(request.json.get('filter'))
    return jsonify([{"id": documentOperationResponses.plainDocument.metadata.id.id,
                    "content": documentOperationResponses.plainDocument.content.content.hex(),
                    "type": documentOperationResponses.plainDocument.metadata.type.name,
                    "size": documentOperationResponses.plainDocument.metadata.size,
                    "uploadDate": documentOperationResponses.plainDocument.metadata.uploadTime,
                    "status": documentOperationResponses.documentStatus.status.name}])