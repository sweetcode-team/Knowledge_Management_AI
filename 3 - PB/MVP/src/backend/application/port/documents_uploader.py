from typing import List
from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse
from domain.document_id import DocumentId

class DocumentsUploader:
    def uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]:
        return [DocumentOperationResponse(DocumentId("Documento.pdf"), True, "Document uploaded successfully")]