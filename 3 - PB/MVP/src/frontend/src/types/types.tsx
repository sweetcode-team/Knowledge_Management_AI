import { LucideIcon } from "lucide-react";

import { z } from "zod";

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
    id: number
    status: boolean
    message: string
}

export type ChatPreview = {
    id: number
    title: string
    lastMessage: Message
}

// MESSAGE

export type Message = {
    content: string
    timestamp: string
    sender: string
    relevantDocuments?: string[]
}

export type MessageResponse = {
    chatId: string
    status: boolean
    messageResponse: Message
}

// DOCUMENT

export enum Status {
    CONCEALED = 1,
    ENABLED = 2,
    NOT_EMBEDDED = 3,
    INCONSISTENT = 4
}

export type DocumentWithContent = {
    id: string
    type: string
    size: number
    content: string
    uploadTime: string
    status: Status
}

export type LightDocument = {
    id: string
    type: string
    size: number
    uploadTime: string
    status: string
}

export type DocumentOperationResponse = {
    id: string
    status: boolean
    message: string
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

export const LLMConfigurationFormSchema = z.object({
    LLMModel: z.string()
})

export type LLMConfigurationFormValues = z.infer<typeof LLMConfigurationFormSchema>

export const configurationFormSchema = z.object({
    LLMModel: z.string(),
    vectorStore: z.string(),
    embeddingModel: z.string(),
    documentStore: z.string()
})

export type ConfigurationFormValues = z.infer<typeof configurationFormSchema>

export const askChatbotFormSchema = z.object({
    chatId: z.number().optional(),
    message: z.string()
})

export type AskChatbotFormValues = z.infer<typeof askChatbotFormSchema>

export const renameChatFormSchema = z.object({
    chatId: z.coerce.number(),
    title: z.string().min(1).max(70).trim(),
})

export type RenameChatFormValues = z.infer<typeof renameChatFormSchema>
