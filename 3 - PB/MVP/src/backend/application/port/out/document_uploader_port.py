from typing import List

from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse


class DocumentUploaderPort:
    def uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]:
        pass