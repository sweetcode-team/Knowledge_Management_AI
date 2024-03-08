from flask import request, Blueprint, jsonify

from adapter._in.web.get_documents_controller import GetDocumentsController
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from adapter.out.get_documents.get_documents_list_awss3 import GetDocumentsListAWSS3
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort
from application.service.get_documents_facade_service import GetDocumentsFacadeService
from application.service.get_documents_metadata import GetDocumentsMetadata
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

getDocumentsBlueprint = Blueprint("getDocuments", __name__)


@getDocumentsBlueprint.route("/getDocuments", methods=['POST'])
def getDocuments():
    controller = GetDocumentsController(GetDocumentsFacadeService(GetDocumentsMetadata(GetDocumentsListAWSS3(AWSS3Manager())),
                                                                  GetDocumentsStatus(GetDocumentsStatusVectorStore(VectorStoreChromaDBManager()))))
    documentOperationResponses = controller.getDocuments(request.json.get('filter'))
    return documentOperationResponses