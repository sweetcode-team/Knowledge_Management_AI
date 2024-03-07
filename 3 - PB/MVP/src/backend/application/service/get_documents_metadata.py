from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort


class GetDocumentsMetadata:
    def __init__(self, outPort: GetDocumentsMetadataPort):
        self.outPort = outPort

    def getDocumentsMetadata(self, documentFilter: DocumentFilter) -> List[DocumentMetadata]:
        return self.outPort.get_documents_metadata(documentFilter)
