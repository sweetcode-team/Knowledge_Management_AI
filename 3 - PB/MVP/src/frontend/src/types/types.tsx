import { LucideIcon } from "lucide-react";

export type NavItems = {
    title: string
    path: string
    icon: LucideIcon
}

// CHAT

export type Chat = {
    id: number
    title: string
    messages: Message[]
}

export type ChatOperationResponse = {
    chatId: number
    status: boolean
    message: string
}

export type ChatPreview = {
    chatId: number
    title: string
    lastMessage: Message
}

// MESSAGE

export enum MessageSender {
    USER = 1,
    CHATBOT = 2
}

export type Message = {
    content: string
    timestamp: string
    sender: MessageSender
    relevantDocuments: DocumentId[]
}

export type MessageResponse = {
    chatId: string
    status: boolean
    messageResponse: Message
}

// DOCUMENT

export type DocumentId = {
    id: string
}

export enum Status {
    CONCEALED = 1,
    ENABLED = 2,
    NOT_EMBEDDED = 3,
    INCONSISTENT = 4
}
export type DocumentContent = {
    id: string
    type: string
    size: number
    content: string
    uploadDate: string
    status: Status
}

export type DocumentMetadata = {
    id: string
    type: string
    size: number
    uploadDate: string
    status: string
}

export type DocumentOperationResponse = {
    status: boolean
    message: string
    documentId: string
}

// CONFIGURATION

export type VectorStore = {
    name: string
    type: string
    description: string
    organization: string
    costIndicator: string
}

export type EmbeddingsModel = {
    name: string
    type: string
    description: string
    organization: string
    costIndicator: string
}

export type LLMModel = {
    name: string
    type: string
    description: string
    organization: string
    costIndicator: string
}

export type DocumentStore = {
    name: string
    type: string
    description: string
    organization: string
    costIndicator: string
}

export type Configuration = {
    vectorStore: VectorStore
    embeddingModel: EmbeddingsModel
    LLMModel: LLMModel
    documentStore: DocumentStore
}

export type ConfigurationOperationResponse = {
    status: boolean
    message: string
}

export type ConfigurationOptions = {
    vectorStores: VectorStore[]
    embeddingModels: EmbeddingsModel[]
    LLMModels: LLMModel[]
    documentStores: DocumentStore[]
}

