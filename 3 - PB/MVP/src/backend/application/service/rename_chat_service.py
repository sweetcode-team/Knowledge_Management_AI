from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from application.port._in.rename_chat_use_case import RenameChatUseCase
from application.port.out.rename_chat_port import RenameChatPort

"""
This class is the implementation of the RenameChatUseCase interface.
    Attributes:
        outPort (RenameChatPort): The port to use to rename the chat.
"""
class RenameChatService(RenameChatUseCase):
    def __init__(self, renameChatPort: RenameChatPort):
        self.outPort = renameChatPort
            
    """
    Renames the chat and returns the response.
    Args:
        chatId (ChatId): The chat id.
        title (str): The new title of the chat.
    """ 
    def renameChat(self, chatId: ChatId, title: str) -> ChatOperationResponse:
        return self.outPort.renameChat(chatId, title)