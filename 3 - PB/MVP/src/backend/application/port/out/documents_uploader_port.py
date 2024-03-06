from typing import List

from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse


class DocumentsUploaderPort:
    def uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]:
        pass