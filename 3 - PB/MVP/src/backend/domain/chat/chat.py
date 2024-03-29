from dataclasses import dataclass
from typing import List

from domain.chat.chat_id import ChatId
from domain.chat.message import Message

"""
Chat: classe che rappresenta una chat
    Attributes:
        title (str): Il titolo della chat
        chatId (ChatId): L'identificativo della chat
        messages (List[Message]): La lista dei messaggi della chat
"""
@dataclass
class Chat:
    title: str
    chatId: ChatId
    messages: List[Message]