from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata


class GetDocumentsMetadataPort:
    def get_documents_metadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        pass