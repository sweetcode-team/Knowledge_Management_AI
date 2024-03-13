from langchain.chains.base import Chain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.messages import get_buffer_string

from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.message import MessageSender
from domain.document.document_id import DocumentId

from application.port.out.ask_chatbot_port import AskChatbotPort

from datetime import datetime, timezone

from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel
from adapter.out.persistence.postgres.chat_history_manager import ChatHistoryManager


class AskChatbotLangchain(AskChatbotPort):
    def __init__(self, chain: Chain, chatHistoryManager: ChatHistoryManager):
        self.chain = chain
        self.chatHistoryManager = chatHistoryManager
    
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        if chatId is not None:
            chatHistory = self.chatHistoryManager.getChatHistory(chatId.id)
            if len(chatHistory.messages) == 0:
                return MessageResponse(status=False, messageResponse=None, chatId=chatId)
            else:
                #TODO: Controllare se 6 messaggi sono sufficienti
                answer = self.chain.invoke({"question": message.content, "chat_history": get_buffer_string(chatHistory.messages[:-6])})
        else:
            answer = self.chain.invoke({"question": message.content, "chat_history": []})

        return MessageResponse(
            status=True,
            messageResponse=Message(
                answer["answer"],
                datetime.now(timezone.utc),
                list(set(DocumentId(relevantDocumentId.metadata.get("source")) for relevantDocumentId in answer["source_documents"])),
                MessageSender.CHATBOT
            ),
            chatId=chatId
        )