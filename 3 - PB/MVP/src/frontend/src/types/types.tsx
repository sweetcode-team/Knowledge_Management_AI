import { LucideIcon } from "lucide-react";

export type NavItems = {
    title: string;
    path: string;
    icon: LucideIcon;
}
export type Chat = {
    id: number;
    title: string;
    messages: Message[];
}
export type ChatOperationResponse = {
    chatId: number;
    status: boolean;
    message: string;
}

export type ChatPreview = {
    chatId: number;
    title: string;
    lastMessage: Message;
}

// ----------------      MESSAGE


export enum MessageSender {
    USER = 1,
    CHATBOT = 2
}

export type Message = {
    content: string;
    timestamp: string;
    sender: MessageSender;
    relevantDocuments: DocumentId[];
}

export type MessageResponse = {
    chatId: string;
    status: boolean;
    messageResponse: Message;
}

// ----------------      DOCUMENT

export type DocumentId = {
    id: string;
}

export enum Status{
    CONCEALED = 1,
    ENABLED = 2,
    NOT_EMBEDDED = 3,
    INCONSISTENT = 4
}
export type DocumentContent = {
    id: string;
    type: string;
    size: number;
    content: string;
    uploadDate: string;
    status: Status;
}

export type DocumentOperationResponse = {
    status: boolean;
    message: string;
    documentId: string;
}
// ----------------      CONFIGURATION

export type VectorStore = {
    costIndicator: string,
    description: string,
    name: string,
    organization: string,
    type: string
}
export type EmbeddingsModel = {
    costIndicator: string,
    description: string,
    name: string,
    organization: string,
    type: string
}
export type LLMModel = {
    costIndicator: string,
    description: string,
    name: string,
    organization: string,
    type: string
}

export type DocumentStore = {
    costIndicator: string,
    description: string,
    name: string,
    organization: string,
    type: string
}

export type Configuration = {
    vectorStore: VectorStore;
    embeddingModel: EmbeddingsModel;
    LLMModel: LLMModel;
    documentStore: DocumentStore;
}
export type ConfigurationOperationResponse = {
    status: boolean;
    message: string;
}

