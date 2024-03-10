from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata


class GetDocumentsMetadataPort:
    def getDocumentsMetadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        pass