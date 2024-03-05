from typing import List

from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse


class EmbeddingsUploaderPort:
    def uploadEmbeddings(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]:
        pass