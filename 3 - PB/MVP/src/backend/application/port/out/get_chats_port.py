from typing import List

from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview


class GetChatsPort:
    def getChats(self, chatFilter: ChatFilter) -> List[ChatPreview]:
        pass