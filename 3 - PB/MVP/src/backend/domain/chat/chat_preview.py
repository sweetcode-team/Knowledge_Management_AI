from dataclasses import dataclass

from domain.chat.chat_id import ChatId
from domain.chat.message import Message

"""
ChatPreview: classe che rappresenta una preview di una chat
    Attributes:
        id (ChatId): L'identificativo della chat
        title (str): Il titolo della chat
        lastMessage (Message): L'ultimo messaggio della chat
"""
@dataclass
class ChatPreview:
    id: ChatId
    title: str
    lastMessage: Message