from typing import List

from application.port._in.get_chats_use_case import GetChatsUseCase
from application.port.out.get_chats_port import GetChatsPort
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview


class GetChatsService(GetChatsUseCase):
    def __init__(self, getChatsPort: GetChatsPort):
        self.getChatsPort = getChatsPort

    def getChats(self, chatFilter: ChatFilter) -> List[ChatPreview]:
        return self.getChatsPort.getChats(chatFilter)

