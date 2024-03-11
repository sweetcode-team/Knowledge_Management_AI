from dataclasses import dataclass

from domain.chat.chat_info import ChatInfo


@dataclass
class ChatPreview:
    def __init__(self, lastMessageSnippet: str, chatInfo: ChatInfo):
        self.lastMessageSnippet = lastMessageSnippet
        self.chatInfo = chatInfo