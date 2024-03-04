from typing import List
from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse
from domain.document_id import DocumentId

class EmbeddingsUploader:
    def uploadEmbeddings(self, documents:List[Document]) -> List[DocumentOperationResponse]:
        return [DocumentOperationResponse(DocumentId("Documento.pdf"), True, "Embeddings uploaded successfully")]