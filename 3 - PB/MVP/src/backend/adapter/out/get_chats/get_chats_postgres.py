from typing import List

from application.port.out.get_chats_port import GetChatsPort
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

"""
This class is the implementation of the GetChatsPort interface. It uses the PostgresChatORM to get the chats.
    Attributes:
        postgresORM (PostgresChatORM): The PostgresChatORM to use to get the chats.
"""
class GetChatsPostgres(GetChatsPort):
    def __init__(self, postgresORM: PostgresChatORM):
        self.postgresORM = postgresORM
        
    """
    Gets the chats and returns the chat previews.
    Args:
        chatFilter (ChatFilter): The chat filter.
    Returns:
        List[ChatPreview]: The chat previews.
    """    
    def getChats(self, chatFilter: ChatFilter) -> List[ChatPreview]:
        chatsPreview = []
        listOfChatPreview = self.postgresORM.getChats(chatFilter.searchFilter)
        for chatPreview in listOfChatPreview:
            previewOfChat = chatPreview.getChatPreview()
            chatsPreview.append(previewOfChat)
        return chatsPreview
