from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

class RenameChatUseCase:
    def renameChat(self, chatId: ChatId, titel: str) -> ChatOperationResponse:
        pass