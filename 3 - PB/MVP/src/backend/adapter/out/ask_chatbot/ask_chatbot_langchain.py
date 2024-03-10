from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.message import MessageSender
from domain.document.document_id import DocumentId

from application.port.out.ask_chatbot_port import AskChatbotPort

from datetime import datetime, timezone

class AskChatbotLangchain(AskChatbotPort):
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        return MessageResponse(
            True,
            Message(content="I'm a chatbot, this is my response.", timestamp=datetime.now(timezone.utc), relevantDocuments=[DocumentId("DocumentoRilevante.pdf")], sender=MessageSender.CHATBOT),
            chatId
        )