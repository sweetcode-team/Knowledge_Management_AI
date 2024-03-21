export type VectorStore = {
    costIndicator: string
    description: string
    name: string
    organization: string
    type: string
}

export type EmbeddingsModel = {
    costIndicator: string
    description: string
    name: string
    organization: string
    type: string
}

export type LLMModel = {
    costIndicator: string
    description: string
    name: string
    organization: string
    type: string
}

export type DocumentStore = {
    costIndicator: string
    description: string
    name: string
    organization: string
    type: string
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