from dataclasses import dataclass

from domain.chat.chat_id import ChatId

"""
ChatOperationResponse: classe che rappresenta la risposta di un'operazione su una chat
    Attributes:
        chatId (ChatId): L'identificativo della chat
        status (bool): Lo stato dell'operazione
        message (str): Il messaggio dell'operazione
"""
@dataclass
class ChatOperationResponse:
    chatId: ChatId
    status: bool
    message: str
    
    def ok(self) -> bool:
        return self.status