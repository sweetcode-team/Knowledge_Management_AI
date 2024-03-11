from typing import List

from domain.chat.chat_id import ChatId
from domain.chat.message import Message


class Chat:
    def __init__(self, title:str, chatId: ChatId, messages: List[Message]):
        self.title = title
        self.chatId = chatId
        self.messages = messages