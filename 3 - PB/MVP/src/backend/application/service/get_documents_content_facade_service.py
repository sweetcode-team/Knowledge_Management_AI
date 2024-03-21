from typing import List

from application.port._in.get_documents_content_use_case import GetDocumentsContentUseCase
from domain.document.document import Document
from domain.document.document_id import DocumentId
from application.service.get_documents_status import GetDocumentsStatus
from application.service.get_documents_content import GetDocumentsContent

from domain.exception.exception import ElaborationException

"""
    A service that gets the content of documents.
Methods:
    getDocumentsContent(self, documentIds:List[DocumentId]) -> List[Document]: 
        Gets the content of a list of documents.
"""
class GetDocumentsContentFacadeService(GetDocumentsContentUseCase):
    def __init__(self, documentContentGetter: GetDocumentsContent, getDocumentsStatus: GetDocumentsStatus):
        self.documentContentGetter = documentContentGetter
        self.getDocumentsStatus = getDocumentsStatus

    
    """
    Gets the content of a list of documents.
    Args:
        documentIds (List[DocumentId]): The documents to get the content.
    Returns:
        List[Document]: The documents with the content.
    """ 
    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[Document]:
        documentsContent = self.documentContentGetter.getDocumentsContent(documentIds)
        documentsStatus = self.getDocumentsStatus.getDocumentsStatus(documentIds)
        
        if len(documentsContent) != len(documentsStatus):
            raise ElaborationException("Errore nel recupero dei contenuti dei documenti.")
        
        documents = []
        for documentContent, documentStatus in zip(documentsContent, documentsStatus):
            document = Document(plainDocument=documentContent, documentStatus=documentStatus)
            documents.append(document)
        return documents
