from typing import List

from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview

"""
This interface is the input port of the GetChatsUseCase. It is used to get the chats.
"""
class GetChatsUseCase:
       
    """
    Gets the chats and returns the chat previews.
    Args:
        chatFilter (ChatFilter): The chat filter.
    Returns:
        List[ChatPreview]: The chat previews.
    """ 
    def getChats(self, chatFilter: ChatFilter) -> List[ChatPreview]:
        pass