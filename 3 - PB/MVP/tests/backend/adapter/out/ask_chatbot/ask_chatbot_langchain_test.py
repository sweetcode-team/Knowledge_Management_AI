from langchain.chains import ConversationalRetrievalChain
from langchain.chains.base import Chain

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
            self.chain.memory = self.chatHistoryManager.getChatHistory(chatId)
            print(self.chatHistoryManager.getChatHistory(chatId.id).messages, flush=True)
            answer = self.chain.invoke({"question": message.content})
        else:
            answer = self.chain.invoke({"question": message.content, "chat_history": ""})

        return MessageResponse(
            True,
            Message(
                answer["answer"],
                datetime.now(timezone.utc),
                list(set(DocumentId(relevantDocumentId.metadata.get("source")) for relevantDocumentId in answer["source_documents"])),
                MessageSender.CHATBOT
            ), chatId
        )