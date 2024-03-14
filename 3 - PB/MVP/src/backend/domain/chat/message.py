from datetime import datetime
from typing import List
from enum import Enum
from domain.document.document_id import DocumentId
from dataclasses import dataclass

"""
MessageSender: enum che rappresenta il mittente di un messaggio
    Attributes:
        USER (int): Il mittente è l'utente
        CHATBOT (int): Il mittente è il chatbot
"""
@dataclass
class MessageSender(Enum):
    USER = 1
    CHATBOT = 2

"""
Message: classe che rappresenta un messaggio
    Attributes:
        content (str): Il contenuto del messaggio
        timestamp (datetime): Il timestamp del messaggio
        relevantDocuments (List[DocumentId]): La lista dei documenti rilevanti al messaggio
        sender (MessageSender): Il mittente del messaggio
"""
@dataclass
class Message:
    content: str
    timestamp: datetime
    relevantDocuments: List[DocumentId]
    sender: MessageSender