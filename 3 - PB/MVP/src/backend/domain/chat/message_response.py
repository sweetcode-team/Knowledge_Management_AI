from dataclasses import dataclass
from domain.chat.message import Message
from domain.chat.chat_id import ChatId

"""
MessageResponse: classe che rappresenta la risposta di un'operazione su un messaggio
    Attributes:
        chatId (ChatId): L'identificativo della chat
        status (bool): Lo stato dell'operazione
        messageResponse (Message): Il messaggio dell'operazione
"""
@dataclass
class MessageResponse:
    chatId: ChatId
    status: bool
    messageResponse: Message
    
    def ok(self) -> bool:
        return self.status