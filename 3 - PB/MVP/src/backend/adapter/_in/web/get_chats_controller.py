from typing import List

from application.port._in.get_chats_use_case import GetChatsUseCase
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview

"""
This class is the controller for the use case GetChatsUseCase. It receives the search filter and returns a list of ChatPreview.
Attributes:
    useCase (GetChatsUseCase): The use case for getting chats.
"""
class GetChatsController:
    def __init__(self, getChatsUseCase: GetChatsUseCase):
        self.useCase = getChatsUseCase
  
    def getChats(self, searchFilter:str)-> List[ChatPreview]:
        """
        Receives the search filter and returns a list of ChatPreview.
        Args:
            searchFilter (str): The search filter.
        Returns:
            List[ChatPreview]: the list of ChatPreview that match the search filter.
        """
        filter = ChatFilter(searchFilter)
        return self.useCase.getChats(filter)