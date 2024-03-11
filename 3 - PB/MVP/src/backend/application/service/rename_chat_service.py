from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from application.port._in.rename_chat_use_case import RenameChatUseCase
from application.port.out.rename_chat_port import RenameChatPort

class RenameChatService(RenameChatUseCase):
    def __init__(self, renameChatPort: RenameChatPort):
        self.outPort = renameChatPort
        
    def renameChat(self, chatId: ChatId, title: str) -> ChatOperationResponse:
        self.outPort.renameChat(chatId, title)