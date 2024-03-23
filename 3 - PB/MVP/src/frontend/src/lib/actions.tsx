"use server"

import {
    AskChatbotFormValues,
    Chat,
    ChatOperationResponse,
    ChatPreview,
    Configuration,
    ConfigurationOperationResponse,
    ConfigurationOptions,
    DocumentContent,
    DocumentMetadata,
    DocumentOperationResponse,
    MessageResponse
} from "@/types/types"
import { revalidatePath, revalidateTag } from "next/cache";
import { ConfigurationFormValues } from '../types/types';

export async function askChatbot(formData: AskChatbotFormValues): Promise<MessageResponse> {
    try {
        const response = await fetch('http://localhost:4000/askChatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(formData as any).toString(),
        })
        revalidateTag("chat")
        return response.json()
    } catch (e) {

    }
}

export async function changeConfiguration(formData: ConfigurationFormValues): Promise<ConfigurationOperationResponse> {
    const response = await fetch('http://localhost:4000/changeConfiguration', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(formData.toString())
    })
    revalidateTag("configuration")

    return response.json()
}

export async function concealDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`http://localhost:4000/concealDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function deleteChats(ids: number[]): Promise<ChatOperationResponse> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('chatIds', id.toString()));
    console.log(formData.toString())
    const result = await fetch(`http://localhost:4000/deleteChats`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("chat")

    return result.json()
}

export async function deleteDocuments(ids: string[]): Promise<DocumentOperationResponse> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`http://localhost:4000/deleteDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function embedDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`http://localhost:4000/embedDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function enableDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`http://localhost:4000/enableDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function getChatMessages(id: number): Promise<Chat> {
    const result = await fetch(`http://localhost:4000/getChatMessages/${id}`,
        {
            next: { tags: ["chat"] }
        }
    )
    return result.json()
}

export async function getChats(filter: string = ""): Promise<ChatPreview[]> {
    const result = await fetch("http://localhost:4000/getChats" + (filter.trim() !== "" ? `/${filter.trim()}` : ""),
        {
            next: { tags: ["chat"] }
        }
    )
    return result.json()
}

export async function getConfigurationOptions(): Promise<ConfigurationOptions> {
    const result = await fetch(`http://localhost:4000/getConfigurationOptions`,
        {
            next: { tags: ["configuration"] }
        }
    )
    return result.json()
}

export async function getConfiguration(): Promise<Configuration> {
    const result = await fetch(`http://localhost:4000/getConfiguration`,
        {
            next: { tags: ["configuration"] }
        }
    )
    return result.json()
}

export async function getDocumentContent(id: string): Promise<DocumentContent> {
    const result = await fetch(`http://localhost:4000/getDocumentContent/${id}`,
        {
            next: { tags: ["document"] }
        }
    )
    return result.json()
}

export async function getDocuments(filter: string = ""): Promise<DocumentMetadata[]> {
    const result = await fetch(`http://localhost:4000/getDocuments` + (filter.trim() !== "" ? `/${filter.trim()}` : ""),
        {
            next: { tags: ["document"] }
        }
    )
    return result.json()
}

export async function renameChat(id: number, title: string): Promise<ChatOperationResponse> {
    const formData = new FormData();
    formData.append('chatId', id.toString());
    formData.append('title', title);
    const result = await fetch(`http://localhost:4000/renameChat`, {
        method: 'POST',
        body: formData
    })
    revalidateTag("chat")

    return result.json()
}

export async function setConfiguration(configuration: Configuration): Promise<ConfigurationOperationResponse> {
    const formData = new FormData();
    formData.append('LLMModel', JSON.stringify(configuration.LLMModel));
    formData.append('documentStore', JSON.stringify(configuration.documentStore));
    formData.append('vectorStore', JSON.stringify(configuration.vectorStore));
    formData.append('embeddingModel', JSON.stringify(configuration.embeddingModel));

    const result = await fetch(`http://localhost:4000/setConfiguration`, {
        method: 'POST',
        body: formData
    })
    revalidateTag("configuration")

    return result.json()
}

export async function uploadDocuments(formData: FormData, forceUpload: boolean = false): Promise<DocumentOperationResponse[]> {
    if (forceUpload) {
        formData.append('forceUpload', 'true')
    }
    const result = await fetch(`http://localhost:4000/uploadDocuments`, {
        method: 'POST',
        body: formData
    })
    revalidateTag("document")

    return result.json()
}