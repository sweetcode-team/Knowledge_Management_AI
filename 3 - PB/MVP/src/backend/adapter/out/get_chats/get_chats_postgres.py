from typing import List

from application.port.out.get_chats_port import GetChatsPort
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM


class GetChatsPostgres(GetChatsPort):
    def __init__(self, postgresORM: PostgresChatORM):
        self.postgresORM = postgresORM
        
    def getChats(self, chatFilter: ChatFilter) -> List[ChatPreview]:
        chatsPreview = []
        listOfChatPreview = self.postgresORM.getChats(chatFilter.searchFilter)
        for chatPreview in listOfChatPreview:
            previewOfChat = chatPreview.getChatPreview()
            chatsPreview.append(previewOfChat)
        return chatsPreview
