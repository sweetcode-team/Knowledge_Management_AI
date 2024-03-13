from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from application.port._in.rename_chat_use_case import RenameChatUseCase

class RenameChatController:
    def __init__(self, renameChatUseCase: RenameChatUseCase):
        self.useCase = renameChatUseCase
        
    def renameChat(self, chatId: int, title: str) -> ChatOperationResponse:
        return self.useCase.renameChat(ChatId(chatId), title)