from unittest.mock import MagicMock, patch

from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.delete_documents import DeleteDocuments
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings
from application.service.delete_documents_service import DeleteDocumentsService


def test_Integration_Delete_Documents_Service():
    DocumentIds = [DocumentId("prova1"), DocumentId("prova2")]
    deleteDocumentsPortMock = MagicMock()
    deleteDocumentsEmbeddingsPortMock = MagicMock()

    service = DeleteDocumentsService(
        DeleteDocuments(deleteDocumentsPortMock),
        DeleteDocumentsEmbeddings(deleteDocumentsEmbeddingsPortMock)
    )

    returnable = service.deleteDocuments(DocumentIds)

    deleteDocumentsPortMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("prova1"), True, "Document deleted"),
                                                            DocumentOperationResponse(DocumentId("prova2"), True, "Document deleted")]
    deleteDocumentsEmbeddingsPortMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("prova1"), True, "Document deleted"),
                                                            DocumentOperationResponse(DocumentId("prova2"), True, "Document deleted")]

    assert returnable == [DocumentOperationResponse(DocumentId("prova1"), True, "Document deleted"),
                                                            DocumentOperationResponse(DocumentId("prova2"), True, "Document deleted")]
