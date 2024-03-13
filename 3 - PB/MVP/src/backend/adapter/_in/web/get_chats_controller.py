from typing import List

from application.port._in.get_chats_use_case import GetChatsUseCase
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview



class GetChatsController:
    def __init__(self, getChatsUseCase:GetChatsUseCase):
        self.useCase = getChatsUseCase

    def getChats(self, searchFilter: str)-> List[ChatPreview]:
        filter = ChatFilter(searchFilter)
        return self.useCase.getChats(filter)